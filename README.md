# Task Manager

A FastAPI-based application for managing tasks!

## Overview

Task Manager is a backend application built with FastApi that allows users to create, view, and delete tasks. The frontend is served through FastAPI’s interactive docs, which makes it easy to interact with the API directly.

## Architecture

- The application consists of **two replicated FastAPI servers**.
- Each server is connected to a separate **PostgreSQL** database instance.
- The databases are kept in sync using **bidirectional logical replication**, a feature introduced in **PostgreSQL 16**.

## Features

- ✅ Create new tasks  
- ❌ Delete tasks  
- 🔍 View existing tasks  

### Each Task Contains:

- `id`: Unique identifier
- `title`: Task's title 
- `description`: Task's description  
- `assignee`: Assigned user for the task  
- `creation_time`: Timestamp when the task was created

### Testing
- Integration tests to make sure all DB functionalities work, including adding new tasks, deleting tasks and synchronizing the DBs
- Run "make integration-test" to execute the tests

## License

MIT License
