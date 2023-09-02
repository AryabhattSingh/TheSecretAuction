# The Secret Auction

Welcome to The Secret Auction! This project is a simple Python program designed to facilitate a silent auction by taking input from bidders and displaying 
the winner at the end.

## Overview

The objective of The Silent Auction is to create a fun and interactive way to conduct a silent auction. Here's how it works:

1. The program displays a captivating `ASCII art` of a gavel, setting the auction atmosphere.

2. The user, acting as a bidder, is prompted to enter their `name` and `bid amount`.

3. Exception handling is implemented to ensure that the user enters a valid bid amount. If an invalid value is entered, the program will provide a message and prompt the
    user to enter a valid amount.

4. After entering a valid bid amount, the program asks if there are `other bidders`. It keeps asking until the user enters either `yes` or `no` as these are the valid inputs.

5. If there are more bidders, the terminal screen gets cleared, erasing the previous entry while keeping the ASCII art gavel displayed.

6. The program uses a `dictionary` to store the bidders' names as `keys` and their bid amounts as `values.

7. When there are no more bidders, the program displays the winner's name along with the winning bid amount.

## Usage

To use The Silent Auction program, follow these steps:

1. Clone this GitHub repository to your local machine.

2. Make sure you have Python installed on your computer. You can download it from [Python's official website](https://www.python.org/downloads/).

3. Open your terminal or command prompt and navigate to the directory where you cloned the repository.

4. Run the program by executing the following command:

   ```
   python main.py
   ```

5. Follow the on-screen instructions to enter bidder names and bid amounts. Ensure that you input valid bid amounts and respond with "yes" or "no" when asked if there
 are more bidders.

6. Once all bidders have participated, the program will display the winner's name and the winning bid amount.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request with your changes. We welcome any improvements, bug fixes, or
additional features that can make this silent auction program even better.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Happy Bidding! 🎉🔨
