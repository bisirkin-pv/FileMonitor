# FileMonitor v1.0

> Следит за изменениями файлов и выполняет указанные действия.

Текущее выполняемое действие расчитано на генерацию HTML из файлов asciidoc. 
В будущих версих можно будет выполнять и другие действия.

## Начало работы

* Скачайте исходники любым из доступных способом.
* Установите [asciidoctor](https://bisirkin-pv.github.io/asciidoctor.html)
* Запустите файл *FileMonitor.py* передав ему параметры:

```
$ python FileMonitor.py -p "path/mask"

# path - путь к папке (если не указать будет обрабатывать текущюю директорию)
# mask - регулярное выражения для имен файлов
``` 