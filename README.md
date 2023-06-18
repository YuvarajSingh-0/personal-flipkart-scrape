
# Flipkart Price Notifier <img src="https://logos-world.net/wp-content/uploads/2020/11/Flipkart-Emblem.png" alt="Flipkart Logo" width="50" />

Flipkart Price Notifier is a tool that monitors the prices of products on Flipkart and notifies users of any price changes. It utilizes AWS Lambda service to trigger the price change checks and stores the updated prices in an online JSON cloud storage service called 'npoint.io'. Additionally, it sends notifications to Discord through Discord webhooks.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

The Flipkart Price Notifier is designed to help users keep track of price changes for their favorite products on Flipkart. By utilizing AWS Lambda service, the tool periodically checks for price updates and compares them to previous prices. If a price change is detected, the new price is stored in an online JSON cloud storage service called 'npoint.io'. Additionally, the tool sends a notification to Discord through Discord webhooks, ensuring that users are promptly informed about any price variations.

## Features

- Automatic price change monitoring for Flipkart products
- Integration with AWS Lambda for triggering price change checks
- Storage of updated prices in an online JSON cloud storage service (npoint.io)
- Notification to Discord via Discord webhooks

## Tech Stack

The Flipkart Price Notifier is built using the following technologies:

- **Node.js**: Backend JavaScript runtime environment
- **AWS Lambda**: Serverless compute service for running the price change checks
- **Serverless Framework**: Open-source framework for building and deploying serverless applications
- **npoint.io**: Online JSON cloud storage service for storing the updated prices
- **Discord Webhooks**: Integration for sending notifications to Discord
- **Git**: Version control system for collaboration and code management

## Installation

To install and set up the Flipkart Price Notifier, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/flipkart-price-notifier.git
   ```

2. Navigate to the project directory:

   ```bash
   cd flipkart-price-notifier
   ```

3. Install the required dependencies:

   ```bash
   npm install
   ```

4. Configure the AWS Lambda function:
   - Create an AWS Lambda function and set it up to trigger periodically.
   - Use the provided code in the repository's `lambda_function.js` file for the Lambda function code.
   - Configure the necessary environment variables (e.g., Flipkart product URLs, Discord webhook URL, etc.).
   - Set up any required AWS permissions and roles.

5. Configure the npoint.io JSON cloud storage:
   - Create an account on npoint.io.
   - Obtain the API endpoint for your JSON data storage.

6. Update the code with your configuration details:
   - Open the `serverless.yaml` file and update the necessary variables (e.g., AWS Lambda function name, etc.).

7. Deploy the AWS Lambda function and run the Flipkart Price Notifier.

## Usage

To use the Flipkart Price Notifier, follow these steps:

1. Ensure that the AWS Lambda function is running and triggering periodically.

2. Whenever a price change is detected, the new price will be stored in the npoint.io JSON cloud storage.

3. To receive Discord notifications, make sure you have set up a Discord webhook URL and configured it in the AWS Lambda function.

4. Check your Discord channel for notifications whenever there is a price change.

## Contributing

Contributions are welcome! If you want to contribute to the Flipkart Price Notifier project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your modifications and commit them with descriptive messages:

   ```bash
   git commit -m "Add your commit message here"
   ```

4. Push your changes to the new branch on your forked repository:

   ```bash
   git push origin feature/your-feature-name
   ```
```
Make sure to replace `your-username` with your actual GitHub username and modify any other placeholders or URLs as required for your specific project.
