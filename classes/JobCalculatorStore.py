from .BookSequence import BookSection

class JobCalculatorStore:
    def __init__(self, sections: list[BookSection]|list=[], sort_sections: bool = True):
        # Constants
        self._sorted_sections: list[BookSection] = sections
        self._sections: list[BookSection] = sections
        self._sort_sections: bool = sort_sections
        self.__sort()
        
    def __sort(self):
        self._sorted_sections = sorted(self._sorted_sections, key=lambda section: section.size)
        for i in range(0, len(self._sorted_sections), 2):
            self._sorted_sections.insert(0, self._sorted_sections.pop(i))
    
    def __calculated_book_pages(self):
        page_format: list[BookSection] = []
        section_last_page: int = 0
        sections = self._sections if not self._sort_sections else self._sorted_sections
        for section in sections:
            s: BookSection = BookSection(section.size)
            s.page_list = [page + section_last_page for page in s.page_list]
            page_format.append(s)
            section_last_page += s.size
        return page_format
    
    # Properties

    @property
    def original_sections(self) -> list[BookSection]:
        return self._sections if not self._sort_sections else self._sorted_sections
    
    @property
    def sections(self) -> list[BookSection]:
        return self.__calculated_book_pages()
    
    @property
    def to_dict(self) -> dict:
        return {
            'signatures': [
                {
                    'index': i,
                    'size': section.size,
                    'pages': section.pages
                } for i, section in enumerate(self.sections)
            ],
            'pageArray': [page for section in self.sections for page in section.pages]
        }
        
    
    def add_section(self, section: BookSection):
        self._sorted_sections.append(section)
        self._sections.append(section)
        self.__sort()
        
    def remove_section(self, obj: BookSection):
        self._sorted_sections.remove(obj)
        self._sections.remove(obj)
        
    def sort_sections(self, sort: bool):
        self._sort_sections = sort