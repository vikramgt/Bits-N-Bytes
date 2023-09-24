# Bits-N-Bytes

# Mental Health and Well-Being Website

## Overview

This is a comprehensive mental health and well-being website developed with the aim of addressing the challenges individuals face in the digital age. It offers features to enhance mental health, promote responsible digital usage, and provide support for issues such as information overload, social media pressure, and online harassment.

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Google Docs](https://docs.google.com/document/d/1C-vHRVG8lMH9vuElaSh7YfqhXsM6FxfvRAOUMg3ETtQ/edit?usp=sharing)
## Features

1. **Home Page:** The website's landing page introduces its purpose and intentions.

2. **Mental Health Assessment:** Integrated with machine learning, users can take a mental health assessment test to predict whether they might require consultations or support.

3. **Focus Mode:** Users can engage in screen break sessions of various durations (5, 10, 20, and 30 minutes) to promote healthy screen time habits and engage in productive activities.

4. **Streak Points:** Users earn streak points for daily participation in Focus Mode, which can be redeemed for rewards and goodies. { working on}

5. **Mental Health FAQ:** The website provides a curated repository of mental health information, reducing the need for users to search elsewhere. A search feature is available for easy access to relevant content.

6. **Signup and Signin:** Users can create accounts and log in to access personalized features.

7. **Report Page:** A dedicated reporting system allows users to report instances of cyberbullying, with the website's team providing support to victims.

8. **Color Palette Design:** The website uses a calming color palette to create a soothing user experience.

## Technology Stack

- **Django:** The backend is developed using Django, a high-level Python web framework.
- **HTML, CSS, JavaScript:** The frontend is built with HTML, CSS, and JavaScript to create a user-friendly interface.
- **Machine Learning:** Machine learning models are used for mental health assessments and screen break monitoring.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/vikramgt/Bits-N-Bytes
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Apply database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

1. Access the website by navigating to `http://localhost:8000/` in your web browser.

2. Explore the different features and take advantage of the mental health assessment, Focus Mode, and other resources.

## Future Enhancements

In future updates, we plan to implement the following enhancements:

- **Anonymous User Interactions:** Allow users to interact with others anonymously, fostering a sense of community and support.

- **Screen Break Monitoring:** Implement machine learning to monitor and encourage healthy screen break habits.

- **Global Ranking:** Introduce a ranking system to recognize and reward users for their screen break or study time, promoting motivation.

- **Premium Features:** Add premium services such as newsletters, online consultations with mental health professionals, and an investigation team for more personalized support.

## Contributing

We welcome contributions from the community to improve and expand the website. If you'd like to contribute, please follow our [contributing guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for your purposes.
