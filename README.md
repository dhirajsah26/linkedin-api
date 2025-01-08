# LinkedIn Bulk Messaging Automation

This project automates the process of sending personalized messages to your first-degree LinkedIn connections using Python. The script allows you to send bulk messages with a custom template, personalize them with the recipient's first name, and store the first names in an Excel sheet for future reference.

Here is the LinkedIn post I wrote if you want to follow it :- https://www.linkedin.com/pulse/automating-linkedin-messaging-my-recent-project-dhiraj-sah-qh5yc/?trackingId=PC1VrMfnSxKh0NVEOQVxEg%3D%3D

## Features
- Automatically fetches first-degree LinkedIn connections.
- Sends bulk personalized messages.
- Customizable message templates (personalized with the recipient's first name).
- Option to limit the number of messages sent.
- Prevents rate-limiting by adding a delay between messages.
- Saves first names of recipients in an Excel sheet for reference.

## Prerequisites
- Before running the script, you will need the following:
- Python 3.x installed on your machine.
- linkedin-api Python package installed.
- pandas Python package installed.
- A LinkedIn account for authentication.
- A file (utility.py) containing your LinkedIn credentials (email and password).

## Installation

### Step 1: Install required Python packages

To get started, install the necessary Python packages by running the following command:

```bash
pip install linkedin-api pandas
```
###  Step 2: Clone or download the repository
Clone or download this repository to your local machine.

### Step 3: Create a utility.py file
In the same directory as the script, create a file named utility.py and include your LinkedIn login credentials as shown below:
```bash
# utility.py
email = "your_email@example.com"
password = "your_password"
```
Make sure to replace "your_email@example.com" and "your_password" with your actual LinkedIn

## Usage
Customize the message template in the main() function:

```bash
message_template = "Hello {first_name}, I hope you're doing well!"
```
## Run the script:

```bash
python linkedin_messenger.py
```
The script will authenticate with LinkedIn, fetch your first-degree connections, send personalized messages to them, and save the first names of those messaged into an Excel file called linkedin_first_namesv2.xlsx.
