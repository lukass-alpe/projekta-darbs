class TaskManager:
    def __init__(self):
        # uztaisa jaunu TaskManager objektu ar tukšu uzdevumu sarakstu.
        self.tasks = []

    def add_task(self, task):
        # Pievieno jaunu uzdevumu sarakstam ar nosaukumu un statusu "nav izpildīts".
        self.tasks.append({'task': task, 'done': False})
        print(f'Uzdevums "{task}" veiksmīgi pievienots.')

    def mark_task_as_done(self, task):
        # Atzīmē uzdevumu kā izpildītu, meklējot to pēc nosaukuma sarakstā.
        for t in self.tasks:
            if t['task'] == task:
                t['done'] = True
                print(f'Uzdevums "{task}" atzīmēts kā izpildīts.')
                return
        print(f'Uzdevums "{task}" nav atrasts.')

    def show_tasks(self):
        # Parāda esošos uzdevumus un to izpildes statusus.
        if not self.tasks:
            print('Nav pievienotu uzdevumu.')
            return

        print('\nUzdevumu saraksts:')
        for idx, t in enumerate(self.tasks, start=1):
            status = 'Izpildīts' if t['done'] else 'Nav izpildīts'
            print(f'{idx}. {t["task"]} - {status}')

def main():
    # Izveido TaskManager objektu.
    task_manager = TaskManager()

    while True:
        print('\nIzvēles iespējas:')
        print('1. Pievienot uzdevumu')
        print('2. Atzīmēt uzdevumu kā izpildītu')
        print('3. apskatīt uzdevumus')
        print('4. Iziet no programmas')

        # Lietotāja izvēles iegūšana.
        choice = input('Ievadiet izvēli (1/2/3/4): ')

        if choice == '1':
            # Pievieno uzdevumu, iegūstot nosaukumu no lietotāja.
            task = input('Ievadiet uzdevumu: ')
            task_manager.add_task(task)
        elif choice == '2':
            # Atzīmē uzdevumu kā izpildītu, iegūstot nosaukumu no lietotāja.
            task = input('Ievadiet uzdevumu, ko atzīmēt kā izpildītu: ')
            task_manager.mark_task_as_done(task)
        elif choice == '3':
            # Aplūko esošos uzdevumus.
            task_manager.show_tasks()
        elif choice == '4':
            # Izejoša paziņojuma izvadīšana un programmas beigas.
            print('Programma tiek beigta. Uz redzēšanos!')
            break
        else:
            # Neatbilstošas izvēles paziņojums.
            print('Nepareiza izvēle. Lūdzu, izvélieties citu opciju.')

if __name__ == "__main__":
    main()