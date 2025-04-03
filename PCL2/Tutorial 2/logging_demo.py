import logging

def main():
    """
    A simple demonstration of Python's logging functionality
    focusing on severity levels and message formatting.
    """
    # Configure the basic logger with a custom format
    logging.basicConfig(
        level=logging.DEBUG,  # Capture all levels of messages
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Create a logger for this application
    logger = logging.getLogger('simple_demo')
    
    # Demonstrate the different severity levels
    logger.debug('This is a DEBUG message - detailed information for debugging')
    logger.info('This is an INFO message - confirmation that things are working as expected')
    logger.warning('This is a WARNING message - something unexpected happened but the program still works')
    logger.error('This is an ERROR message - a more serious problem that prevented something from working')
    logger.critical('This is a CRITICAL message - a very serious error that might prevent the program from running')
    
    # Demonstrate including variables in log messages
    user_id = 12345
    items_count = 10
    logger.info(f'User {user_id} has {items_count} items in their cart')
    print(f'User {user_id} has {items_count} items in their cart')
    
    # Demonstrate logging an exception
    
    
    try:
        result = 10 / 0  # This will cause a division by zero error
    except Exception as e:
        logger.error(f'An error occurred: {str(e)}')
        
    logger.info("we got here, yay")

if __name__ == "__main__":
    main()