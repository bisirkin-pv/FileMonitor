# FileMonitor v1.1

> Следит за изменениями файлов и выполняет указанные действия.

Текущее выполняемое действие расчитано на генерацию HTML из файлов asciidoc. 
В ходе работы приложения можно изменить текст команды.

## Начало работы

* Скачайте исходники любым из доступных способом.
* Установите [asciidoctor](https://bisirkin-pv.github.io/asciidoctor.html)
* Запустите файл *FileMonitor.py* передав ему параметры:

```
$ python FileMonitor.py -p "path/mask"

# path - путь к папке (если не указать будет обрабатывать текущую директорию)
# mask - регулярное выражения для имен файлов
``` 

> Доступность ввода команд обозначается **">>"**. Для получения списка команд введите *"help"*

## Описание файлов

### Пакет actions

Пакет **actions** содержит примеры реализации классов выполняемых действий.
Все реализации действий наследуются от `DefaultAction`, тем самым получая необходимые методы.
Для выполнения своих команд необходимо реализовать метод *update(self, monitor)*.

* `DefaultAction` - Шаблон действия
* `AsciiDocGenerateHtmlAction` - Действие по обновлению документации в формате asciiDoc в формат html

### Пакет utilites

Пакет **utilites** содержит вспомогательные классы.

* `Observed` - базовый класс для поддержки оповещения при изменениях.

### Пакет monitor

Пакет **monitor** содержит основные файлы проекта.

* `FileProperty` - именованный кортеж сохраняемых свойств файла
* `Monitor` - класс реализующий основные методы мониторинга, расширяет класс `Observed`
* `Server` - создает отдельный поток для работы мониторинга

### Пакет test

* Тесты для проверки работы приложения

### Пакет src

* `FileMonitor` - реализация CLI интерфейса для работы с мониторингом.
