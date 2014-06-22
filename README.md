Android-XMLView-Extractor
=========================

Extracts the views from an XML and writes the Java code for further functionality

=====
Usage
=====
```
python android_extract_views.py [relative or absolute path to project directory]
i.e. python android_extract_views.py Story-Quilt/
```
Outputs a .java file in the directory the python script is located in, containing the code you would normally use in android.

```
python dup_ids_filter.py [relative or absolute path to res directory]
i.e. python dup_ids_filter.py res/
```
Prints duplicate IDs found with path to file.
