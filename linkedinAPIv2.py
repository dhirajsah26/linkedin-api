from linkedin_api import Linkedin
import time
from typing import List, Dict
import pandas as pd
import utility

class LinkedInMessenger:
    def __init__(self, username: str, password: str):
        """Initialize LinkedIn API client"""
        self.api = Linkedin(username, password)
    
    def get_connections(self, limit: int = None) -> List[Dict]:
        """Get first-degree connections"""
        connections = self.api.search_people(
            network_depths=["F"],  # First-degree connections only
            include_private_profiles=False  # Only public profiles
        )
        
        if limit:
            connections = connections[:limit]
            
        return connections
    
    def send_bulk_messages(self, 
                          message_template: str,
                          limit: int = None,
                          delay: int = 2,
                          personalize: bool = True) -> None:
        """
        Send messages to connections
        
        Args:
            message_template: Message to send (can include {first_name} if personalize=True)
            limit: Maximum number of messages to send
            delay: Delay between messages in seconds
            personalize: Whether to personalize the message with the recipient's name
        """
        first_names_list = []
        # Get connections
        connections = self.get_connections(limit)
        print(f"Found {len(connections)} connections")
        
        success_count = 0
        
        for i, connection in enumerate(connections, 1):
            try:
                # Get profile URN
                profile_urn = connection.get('urn_id')
                
                if personalize:
                    # Get full profile data for personalization
                    profile_data = self.api.get_profile(urn_id=profile_urn)
                    first_name = profile_data.get('firstName', '')
                    
                    message = message_template.format(first_name=first_name)
                    print(message)
                else:
                    message = message_template
                
                # Send message
                self.api.send_message(
                    message_body=message,
                    recipients=[profile_urn]
                )
                
                success_count += 1
                first_names_list.append(first_name)
                print(f"Message sent to connection {i}/{len(connections)}")
                
                # Delay to avoid rate limiting
                time.sleep(delay)
                
            except Exception as e:
                print(f"Failed to send message to connection {i}: {str(e)}")
                continue
        
        print(f"\nCompleted: Successfully sent {success_count} messages out of {len(connections)} connections")
        df = pd.DataFrame(first_names_list, columns=['First Name'])
        df.to_excel("linkedin_first_namesv2.xlsx", index=False)

def main():
    # Your LinkedIn credentials
    USERNAME = utility.email
    PASSWORD = utility.password
    
    # Initialize messenger
    messenger = LinkedInMessenger(USERNAME, PASSWORD)
    
    # Example message template
    message_template = """TEXT"""
    
    messenger.send_bulk_messages(
        message_template=message_template,
        limit=145,  # Limit to 5 connections for testing
        delay=2,  # 2 second delay between messages
        personalize=True  # Use connection's first name
    )

if __name__ == "__main__":
    main()
