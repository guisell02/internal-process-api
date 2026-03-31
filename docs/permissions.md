# Permission Model

The system implements two levels of permissions:

1. Global Roles
2. Process-level Roles

## Global Roles

ADMIN
MEMBER

## Process Roles

OWNER
CONTRIBUTOR
VIEWER

## Permission Matrix

| Action            |       Admin | Owner | Contributor | Viewer |
|------                     |------|------|------       |------|
| Create Process            | ✔    | ❌  | ❌          | ❌ |
| Add Members               | ✔    | ✔   | ❌          | ❌ |
| Create Task               | ✔    | ✔   | ✔           | ❌ |
| Close Process             | ✔    | ✔   | ❌          | ❌ |