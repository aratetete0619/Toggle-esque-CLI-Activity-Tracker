# Activity Tracker

## Overview

`Activity Tracker` is a tool designed to track user activities, providing statistics and reports. As it utilizes Docker, it can be set up easily on any operating system equipped with Docker.

## Installation

1. Clone the repository.

```bash
git clone https://github.com/aratetete0619/activity_tracker.git
```

2. Navigate to the cloned directory.

```bash
cd activity_tracker
```

3. Set up the environment file:

```bash
touch .env
cp .env.sample .env
```

Edit the `.env` file as necessary to configure your settings.

4. Execute `install.sh` to finalize the setup.

```bash
bash install.sh
```

5. After executing the script, the `track` command will be available for use.

## Commands Description

- `start`: Start a new recording.
- `end`: End a recording by specifying its ID.
- `edit`: Modify an existing recording.
- `create`: Create a new record.
- `export`: Export recordings as a CSV file. The exported file will be saved under the `csv` folder, and you can generate CSV files for each month.
- `stats`: Visualize the recorded data.
- `delete_id`: Delete a specific record by ID.
- `delete_all`: Delete all recordings.
- `show`: Display all current records.
- `quit`: Terminate the Activity Tracker.

## Prerequisites

- Docker installed.
