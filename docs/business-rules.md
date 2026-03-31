# Business Rules

## User Management

RULE: Email Uniqueness  
Email must be unique across all users.

RULE: User Deactivation  
Users cannot be deleted physically.
Instead the system performs a soft delete.



## Process Management

RULE: Process Creation  
Only ADMIN users can create processes.

RULE: Process Closure  
A process can only be closed if all tasks
are either COMPLETED or CANCELLED.


## Task Management

RULE: Task Assignment  
A task can only be assigned to a user
who is a member of the same process.