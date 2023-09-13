"""
This program is a notebook app that allows users to create notes, search for
notes, and modify notes. The program is written in Python 3.6.4 and uses the
composition between the class Notebook and the class Note. 


"""

import datetime

class Note:
    """ This class represents a note in the notebook. It will be composed by
    the class Notebook. """
   
    id_count = 0
    def __init__(self, memo, tag):
        self.id = Note.id_count
        Note.id_count += 1
        self.memo = memo
        self.tag = tag
        self.creation_date = datetime.date.today()
    
    def match(self, filter):
        return filter in self.memo or filter in self.tag
    
class Notebook:
    def __init__(self):
        self.notes = []
    
    def new_note(self, memo, tag = ''):
        self.notes.append(Note(memo, tag))
    
    def modify_memo(self, note_id, memo):
        self.notes[note_id].memo = memo

    def modify_tag(self, note_id, tag):
        self.notes[note_id].tag = tag

    def search(self, filter):
        return [note for note in self.notes if note.match(filter)]
    
    def _find_note_by_id(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None
    
    def delete(self, note_id):
        self.notes.remove(self._find_note_by_id(note_id))

    def print_notes(self):
        for note in self.notes:
            print('Note ID: {}'.format(note.id))
            print('Memo: {}'.format(note.memo))
            print('Tag: {}'.format(note.tag))
            print('Creation Date: {}'.format(note.creation_date))
            print('')

    def print_note_addresses(self):
        for i in range(len(self.notes)):
            print(self.notes[i])

if __name__ == '__main__':
    notebook = Notebook()
    notebook.new_note('Hello World')
    notebook.new_note('Hello World again')

    print('notebook.search(\'Hello\'):')
    result = notebook.search('Hello')
    print(result)
   