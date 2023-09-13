"""
This program is a notebook app that allows users to create notes, search for
notes, and modify notes. The program uses composition between the class Notebook and the class Note. 

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
    
    def find_note_by_id(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return f"Note with id {note_id} not found."

    def print_notes(self):
        for note in self.notes:
            print('Note ID: {}'.format(note.id))
            print('Memo: {}'.format(note.memo))
            print('Tag: {}'.format(note.tag))
            print('Creation Date: {}'.format(note.creation_date))
            print('')

    def print_note_memory_addresses(self):
        for note in self.notes:
            print(note)
        
if __name__ == '__main__':
    notebook = Notebook()
    notebook.new_note('Hello World')
    notebook.new_note('Hello World again')

    print('Printing all addresses of notes in the notebook:')
    notebook.print_note_memory_addresses()
    print('')

    print('notebook.notes[0].id: {}'.format(notebook.notes[0].id))
    print('notebook.notes[1].id: {}'.format(notebook.notes[1].id))
    print('notebook.notes[0].memo: {}'.format(notebook.notes[0].memo))
    print()

    print('Executing notebook.search(\'Hello\'):')
    print('Printing all addresses of notes in the notebook with the string \'Hello\' in memo or tag :')
    for note1 in notebook.notes:
        print(note1)
    print('')

    print("Executing notebook.modify_memo(1, 'Hi World')")
    notebook.modify_memo(1, 'Hi World')
    print('notebook.notes[1].memo: {}'.format(notebook.notes[1].memo))

    print("Executing notebook.new_note('With tag', 'Peter')")
    notebook.new_note('With tag', 'Peter')
    print('Printing all addresses of notes in the notebook:')
    notebook.print_note_memory_addresses()
    print('')

    print("Executing vars(notebook.notes[0])")
    print(vars(notebook.notes[0]))
    print()

    print("Executing print(notebook.notes[2].tag)")
    print(notebook.notes[2].tag)

    print("Executing notebook.find_note_by_id(3)")
    note1 = notebook.find_note_by_id(3)
    print(note1)
    print()

    print("Executing notebook.find_note_by_id(2)")
    note2 = notebook.find_note_by_id(2)
    print(vars(note2))
    print()

    print("Executing notebook.modify_tag(2, 'John')")
    notebook.modify_tag(2, 'John')
    print("Executing print(notebook.notes[2].tag)")
    print(notebook.notes[2].tag)
    print()
   
    print('Printing all addresses of notes in the notebook:')
    notebook.print_note_memory_addresses()
    print('')

    print("Printing all notes iterating over the notebook and using vars() for each note:")
    for note in notebook.notes:
        print(vars(note))
    print('')

    print('Printing all notes using print_notes() method:')
    notebook.print_notes()
    




    






    


    

