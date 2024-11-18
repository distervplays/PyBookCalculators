class BookSection:
    def __init__(self, section_size: int):
        # Constants
        self._section_size: int = section_size
        
        page_numbers: dict[str: list] = {
            4: [4, 1, 2, 3],
            8: [6, 3, 4, 5, 8, 1, 2, 7],
            12: [8, 5, 6, 7, 10, 3, 4, 9, 12, 1, 2, 11],
            16: [10, 7, 8, 9, 12, 5, 6, 11, 14, 3, 4, 13, 16, 1, 2, 15],
            20: [12, 9, 10, 11, 14, 7, 8, 13, 16, 5, 6, 15, 18, 3, 4, 17, 20, 1, 2, 19],
            24: [14, 11, 12, 13, 16, 9, 10, 15, 18, 7, 8, 17, 20, 5, 6, 19, 22, 3, 4, 21, 24, 1, 2, 23],
            28: [16, 13, 14, 15, 18, 11, 12, 17, 20, 9, 10, 19, 22, 7, 8, 21, 24, 5, 6, 23, 26, 3, 4, 25, 28, 1, 2, 27],
            32: [18, 15, 16, 17, 20, 13, 14, 19, 22, 11, 12, 21, 24, 9, 10, 23, 26, 7, 8, 25, 28, 5, 6, 27, 30, 3, 4, 29, 32, 1, 2, 31]
        }
        
        self.page_list: list = page_numbers[self._section_size]
        
        # Validations
        if not self.__validate_section_size():
            raise ValueError("Invalid section size, valid section sizes are: 4, 8, 12, 16, 20, 24, 28, 32")

    
    # Properties
    @property
    def pages(self) -> list:
        return self.page_list
    
    @property
    def size(self) -> int:
        return self._section_size
    
    @property
    def section(self) -> dict[str: int, list]:
        return {'size': self._section_size, 'pages': self.pages}
    
    # Private methods
    def __validate_section_size(self) -> bool:
        valid_section_sizes: list = [4, 8, 12, 16, 20, 24, 28, 32]
        return self._section_size in valid_section_sizes
    
    @property
    def to_dict(self) -> dict:
        return {
            'size': self._section_size,
            'pages': self.page_list
        }
    
    # Magic methods
    def __str__(self) -> str:
        return f"Section size: {self._section_size}, Pages: {self.page_list}"
    
    def __repr__(self) -> str:
        return f"Section size: {self._section_size}, Pages: {self.page_list}"
    
    def __eq__(self, other) -> bool:
        return self._section_size == other.size
    
    def __ne__(self, other) -> bool:
        return self._section_size != other.size
    
    def __lt__(self, other) -> bool:
        return self._section_size < other.size
    
    def __le__(self, other) -> bool:
        return self._section_size <= other.size
    
    def __gt__(self, other) -> bool:
        return self._section_size > other.size
    
    def __ge__(self, other) -> bool:
        return self._section_size >= other.size