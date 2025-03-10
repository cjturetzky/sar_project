# Search and Rescue (SAR) Agent Framework - CSC 581

## Introduction

This is an agentic framework for a Rescue Team Leader agent, facilitating communication between the field team and
the operation chief.

## Functions

clear_op(): Resets the team status, member list, and operation status to allow for creation of a new operation

new_op(team_members): Clears the previous operation, before adding all members of team_members to the team list, and notifying them that they are part of a new operation.

update_team_status(status="Status_Here"): Updates the internal status & notifies all team members of the update
status - String describing operation status

update_operation_status(status="Status_Here"): Updates the internal operations status & notifies all team members of the update

add_team_member(member): Adds a new member to the team, and notifies all team members of the new teammate
member - String of the team member's name, creates new RescuerAgent and adds it to internal tracking of team members

get_team_members, get_op_status, get_team_status: Returns the list of team members, operation status, and team status respectively

notify_team(message): Makes a call to google's Gemini API to generate a human readable message, alongside safety and efficiency recommendations.
message - String to send to API before processing and sending to team members

## Insights

- Error Handling: The placeholder of "Unknown" and exception raising for invalid inputs is indeed unhelpful. 
- Testing: There are edge cases, such as multiple team members and unexpected data types, that I fully missed.
- Documentation: The README needs to be a bit more comprehensive. Namely return types and parameters being explicitly described.

## Modifications

- Added prevention for multiples of the same team members being added
- Updated documentation to clarify 
- Updated testing to account for edge cases
- Updated error handler to give more comprehensive messages to users