# Search and Rescue (SAR) Agent Framework - CSC 581

## Introduction

This is an agentic framework for a Rescue Team Leader agent, facilitating communication between the field team and
the operation chief.

## Functions

clear_op(): Resets the team status, member list, and operation status to allow for creation of a new operation

new_op(team_members): Clears the previous operation, before adding all members of team_members to the team list, and notifying them that they are part of a new operation.

update_team_status(status="Status_Here"): Updates the internal status & notifies all team members of the update

update_operation_status(status="Status_Here"): Updates the internal operations status & notifies all team members of the update

add_team_member(member): Adds a new member to the team, and notifies all team members of the new teammate

get_team_members, get_op_status, get_team_status: Returns the list of team members, operation status, and team status respectively
