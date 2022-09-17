class QuickFindUF:
    """
        This is quickfind algorithm. An implementation of dynamic connectivity
        problem.

        Attributes:
            mark_list: This is used for marking the connection between points.
        
        TimeComplexity:
            worst_case: n^2. It initialize N array, process N array and find 1.
    """

    mark_list = []

    def __init__(self, size:int):
        # Initialize the mark array index number to value.
        mark_list = [i for i in range(size)]
    
    def is_connected(self, from_number: int, to_number: int) -> bool:
        """
            This method is responsible for finding out the connection
            between two points.

            Args:
                from_number: An integer number from where connection start.
                to_number: An integer number where connection end.
            
            Returns:
                It returns a boolean value indecate that whether the given
                points are conected or not.
            
            Raises:
                IndexError: If the index is not present in the mar_list.
        """

        return self.mark_list[from_number] == self.mark_list[to_number]
    
    def union(self, from_number: int, to_number: int) -> None:
        """
            This method is responsible for creating connection between
            two points.

            Args:
                from_number: An integer number from where connection start.
                to_number: An integer number where connection end.
            
            Raises:
                IndexError: If the index is not present in the mar_list.
        """

        from_value = self.mark_list[from_number]
        to_value = self.mark_list[to_number]
        
        for key, val in enumerate(self.mark_list):
            if val == to_value:
                self.mark_list[key] = from_value
