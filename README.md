
# Progressive Overload

  

Progressive Overload is a Python-based application designed to help you track and visualize the progress of your workouts. With this tool, you can record exercises, monitor your progress over time, and email your workout plans to yourself.

  ## Table of Contents
  

 - Features
 - Installation
 - Usage

## Features


*  **Record Exercises and Workouts**: Easily add new exercises and log workouts, including sets, reps, and weight.

*  **Track Progress History**: Maintain a detailed history of your workouts, allowing you to see how your performance improves over time.

*  **Visualize Progress**: Generate visual charts to track your progress for each exercise, taking into account sets, reps, and weight.

*  **Email Workout Plans**: Send your workout plans directly to your email for easy access and record-keeping.
 

## Installation

  

To install the project, you'll need Python 3.x and a few additional Python libraries listed in the `requirements.txt` file. Here’s how to set it up:

  

```bash

pip  install  json  os  random  datetime  pytest

  

# Clone the repository

git  clone  https://github.com/MartynasVidziunas/progressive-overload.git

  

# Navigate to the project directory

cd  progressive-overload

  

# Install dependencies

pip  install  -r  requirements.txt
```

## Usage

### Adding an exercise

In the main menu enter 1

![image](https://github.com/user-attachments/assets/f54f86f5-f0c9-4ed3-8383-fb219f0cbdf4)

Then enter 2 in the following menu 

![image](https://github.com/user-attachments/assets/0e4efa0f-3ebb-44ef-a6ba-f7dccad1d6aa)

Now enter the name for the exercise

![image](https://github.com/user-attachments/assets/864a6750-a4a9-4c3f-8620-1160d5047a67)

It's possible to add more than one exercise by typing a name and pressing Enter. Once done type 's' to save the exercises to a file

![image](https://github.com/user-attachments/assets/2ca02199-5800-49fe-b755-f3b73e8ae925)

### Viewing added exercises

In the main menu enter 1

![main menu](https://github.com/user-attachments/assets/6f22c0bd-cbec-4d59-87af-bd76f84f4713)

In the exercise menu enter 1 

![image](https://github.com/user-attachments/assets/897fc4c9-9c17-46e7-889c-c2d3d800c2a3)

If there are exercises saved in the exercises.json file then the first five (or the first page of) exercises should be visible in the terminal

![image](https://github.com/user-attachments/assets/e53ceb85-a403-4296-bf68-bd079ca2180d)

You can navigate through the list by typing 'n' for next page or 'p' for previous

![image](https://github.com/user-attachments/assets/bf986df6-bce6-4c0b-8557-bb4c1b564737)

### Removing an exercise

In the main menu enter 1

![main menu](https://github.com/user-attachments/assets/6f22c0bd-cbec-4d59-87af-bd76f84f4713)

In the exercise menu enter 1 

![image](https://github.com/user-attachments/assets/897fc4c9-9c17-46e7-889c-c2d3d800c2a3)

If there are exercises saved in the exercises.json file then the first five (or the first page of) exercises should be visible in the terminal

![image](https://github.com/user-attachments/assets/e53ceb85-a403-4296-bf68-bd079ca2180d)

You can navigate through the list by typing 'n' for next page or 'p' for previous

![image](https://github.com/user-attachments/assets/bf986df6-bce6-4c0b-8557-bb4c1b564737)

To remove an exercise type in 'r' while viewing the list of exercises and entering the number displayed on the left of the exercise

![image](https://github.com/user-attachments/assets/669d6e0f-5559-485e-a2dd-38edaa28702d)

![image](https://github.com/user-attachments/assets/791323a0-d85a-4aa0-a480-1f566936aa72)

### Adding a workout

In the main menu enter 2

![image](https://github.com/user-attachments/assets/058cfce5-412e-4199-b207-dd0feea150cb)

In the workout menu enter 2

![image](https://github.com/user-attachments/assets/50a0f377-4e3f-4006-b9cf-5dc4a17e1a2c)

Enter the workout name

![image](https://github.com/user-attachments/assets/a10e7418-9152-44fc-8172-aecfe328aa20)

You'll need to enter atleast three exercises per workout. If the exercise was not found in the saved exercises you'll be prompted if you want to add the new exercise

![image](https://github.com/user-attachments/assets/18cc603c-4dfe-4296-969a-66893fdcb075)

Enter the number of sets, reps and weight for the exercise

![image](https://github.com/user-attachments/assets/bb145679-4be5-4cc3-a78e-7c2f09c7d441)

Once you're done adding atleast 3 exercises type 's' to save the workout

![image](https://github.com/user-attachments/assets/b9656df6-bb82-4afd-8d26-196d94821b6f)

### Viewing saved workouts

In the main menu enter 2

![image](https://github.com/user-attachments/assets/058cfce5-412e-4199-b207-dd0feea150cb)

In the workout menu enter 1

![image](https://github.com/user-attachments/assets/35bac31b-7768-49fe-ae16-5927d3d09acc)

If there are any workouts saved in the workouts.json file then the first five (or the first page of) workouts should be visible in the terminal

![image](https://github.com/user-attachments/assets/fa1a6e99-5275-4aae-aa9c-1b21fea8b99b)

You can navigate through the list by typing 'n' for next page or 'p' for previous

### Removing a workout

In the main menu enter 2

![image](https://github.com/user-attachments/assets/058cfce5-412e-4199-b207-dd0feea150cb)

In the workout menu enter 1

![image](https://github.com/user-attachments/assets/35bac31b-7768-49fe-ae16-5927d3d09acc)

If there are any workouts saved in the workouts.json file then the first five (or the first page of) workouts should be visible in the terminal

![image](https://github.com/user-attachments/assets/fa1a6e99-5275-4aae-aa9c-1b21fea8b99b)

To remove a workout type in 'r' while viewing the list of workouts and entering the number displayed on the left of the workout

![image](https://github.com/user-attachments/assets/35bdfcec-3b12-4e18-9af5-5eef0e5dc8ae)

![image](https://github.com/user-attachments/assets/ee2935f9-1e26-4c01-b33f-0f3506d94e47)

### Recording performance

In the main menu enter 2

![image](https://github.com/user-attachments/assets/058cfce5-412e-4199-b207-dd0feea150cb)

In the workout menu enter 3

![image](https://github.com/user-attachments/assets/1fd8eba8-2bd1-41af-8098-774091339946)

Pick a workout fromt he number of saved workouts

![image](https://github.com/user-attachments/assets/5bf8e5d2-2db7-43a2-912a-cad8b62e6732)

For each exercise in the selected workout you'll be prompted to enter the number of sets, reps and weights used for your latest exercise

![image](https://github.com/user-attachments/assets/f518bac1-5361-41b5-b8d2-04d64b457e25)

### E-mailing the workout plan

For this to work you'll need to add an .env file to the 'mail' folder with the following code

![image](https://github.com/user-attachments/assets/51cc006a-08ab-4925-8d25-748c57c51594)

I used a google account with an app password to make it work

In the main menu enter 2

![image](https://github.com/user-attachments/assets/058cfce5-412e-4199-b207-dd0feea150cb)

Enter the email of the receiver

![image](https://github.com/user-attachments/assets/227e681b-8cf4-4ddb-82c1-56337138f708)

Select the workout you want to email

![image](https://github.com/user-attachments/assets/07a2613f-b638-4961-87c7-ee8e77f17097)

If everything went smoothly you'll see this message in the terminal

![image](https://github.com/user-attachments/assets/a6345cfc-758c-47df-b4f0-e72d591fa66a)




