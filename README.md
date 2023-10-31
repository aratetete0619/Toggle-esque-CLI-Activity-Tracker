# Toggle-esque CLI Activity Tracker

## Overview

`Toggle-esque CLI Activity Tracker` is a tool designed to track user activities, providing statistics and reports. As it utilizes Docker, it can be set up easily on any operating system equipped with Docker.

[![Image from Gyazo](https://i.gyazo.com/90f77b6e847167147d4a818ea578aea6.gif)](https://gyazo.com/90f77b6e847167147d4a818ea578aea6)

## Installation

1. Clone the repository.
    ```bash
    git clone https://github.com/aratetete0619/Toggle-esque-CLI-Activity-Tracker.git
    ```

2. Navigate to the cloned directory.
    ```bash
    cd Toggle-esque-CLI-Activity-Tracker
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

6. Source your shell configuration file to apply changes:
    If you're using Zsh:
    ```bash
    source $HOME/.zshrc
    ```

    Or if you're using Bash:
    ```bash
    source $HOME/.bashrc
    ```

7. After executing the script, the `track` command will be available for use.
    ```bash
    track
    ```


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

## Contributing

Thank you for considering contributing to Activity Tracker! Here are some guidelines to keep in mind:

- **Adding Commands**: If you're adding new commands, please create them as individual files under the `services` directory.
  
- **Utility Functions**: If you create functions that might be reused across different parts of the application, consider placing them in the `services/utils` directory.

- **Pull Requests**: When making pull requests, please follow the Git Flow methodology. Direct your pull requests towards the `develop` branch.

We appreciate your efforts in making Activity Tracker better. Happy coding!

