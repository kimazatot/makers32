'''GIT'''
# распределенная система контроля версий (система, записывающая изменения в файле или наборе файлов). Используется для отслеживания и ведения истории изменения файлов, позволяет вернуть старую версию кода

'''GitHub'''
# онлайн сервис - который предоставляет услуги по хранению репозиториев и управлению доступом (аналоги GitLab, Bitbucket)

'commands(порядок отправки на гитхаб)'
# 1. git init -> превращает директорию в гит репозиторий
# (инициализируете директорию и появляется скрытая директория .git) вводится всего один раз

# 2. git add .(все содержимое директории) / 
# <filename> (конкретный файл git add test.py) -> отслеживание файлов или файла гитом

# 3. git commit -m 'message' -> создание коммита с комментом, сохранение в gitе(локально на компе)

# 4. git remote add <название_связи> (обычно origin) ссылка_на_удаленный_репозиторий 
# (HTTPS/SSH) -> связываем локальный репозиторий с удаленным

# 5. git push <название_связи> <название_ветки> (master/main) 
# -> отправка версий кода, на удаленный репозиторий (т.е на гитхаб)

'''команды при повторной отправке на гитхаб'''
# git add .
# git commit -m 'updated'
# git push origin master

'''======================================================================================================'''
# git log -> просмотр журнала с коммитами

# git checkout <hash_commit> -> переключиться к другому коммиту, или другой версии кода

# git status -> проверка статуса файлов

# git pull <branch> -> стягивает изменения с удаленного репозитория,
# с указанной ветки (добавить в локальные файлы, изменения с гитхаба)

# git clone <ссылка_на_удаленный_репозиторий>  -> склонировать/скопировать удаленный репозиторий


'glkfg'