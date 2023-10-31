# Activity Tracker

## Overview

`Activity Tracker` is a tool designed to track user activities, providing statistics and reports. As it utilizes Docker, it can be set up easily on any operating system equipped with Docker.

## Installation

以下のように、手順3と4の間に新しい手順を追加しました：

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

4. Update the `create_user.sql` file:

Based on the values you configured in the `.env` file, replace the placeholders in the `create_user.sql` file.

```sql
CREATE USER 'your_username' @'%' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON ActivityTracker.* TO 'your_username' @'%';
```

Make sure to replace `your_username` and `your_password` with the respective values from the `.env` file.

5. Execute `install.sh` to finalize the setup.

```bash
bash install.sh
```

6. After executing the script, the `track` command will be available for use.

```bash
track
```

## Commands Description
... (残りの内容は変更していません) ...

このように、設定ファイルの値をSQLファイルに適切に置き換えることを明示的に指示する手順を追加しました。

## Commands Description
After executing 'track' on the terminal,

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
