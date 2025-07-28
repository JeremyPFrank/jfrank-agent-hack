"""Main entry point for the report generation workflow.

This code is a simple example of how to use the report generation workflow.
"""

import logging

from . import write_report

logging.basicConfig(level=logging.INFO)
user_input_topic = input("please enter a short paragraph outlining your fitness goals and experience and days per week: ")
print("Generating plan based on your input...")
result = write_report(
    topic=user_input_topic,
    report_structure="""This report develops a week of weightlifting workouts for the user.

The report structure should include:
1. Introduction (no research needed)
- Brief overview of the user's fitness goals and preferences entered by the user (topic)
- express excitement about elevating the user's fitness journey including some of their entered details

2. Main Body Sections:
- One dedicated section for EACH day of the week where each is either labeled a workout or rest day based on the number of days the user wants to work out
- Each section should include:
- Daily exercise list (bulleted list)
- Each Exercise should include:
- ideal sets and reps and effort percentage (bulleted list)
- tips for each exercise to perform better to align to the user's goals (1 sentence)

3. No Main Body Sections other than the ones dedicated to each offering in the user-provided list

4. Conclusion
- include links to research that you used with 1 sentence summaries of each

Things to include: don't output anything related to this section 
- do not overwork the user - make sure to work in proper recovery and keep reps and sets the correct volume based on research
- Make sure to note that you can include saturday and sunday if needed 
- if the user says they want to work out 5 days per week there should be 5 workouts and 2 rest days (7 day week)
- similar if user enters 3 days per week (this leaves 4 rest days)
- Do not re-research for each day; you should do all your research upfront and then use that research to create the workout plan
- make sure each day builds on the others (repeat each exercise at most twice weekly and never on consecutive days)

""",
)
if result:
    print("\n\n" + result["report"] + "\n\n")
