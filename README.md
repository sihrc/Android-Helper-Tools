=====
Android-Helper-Tools
=====

Useful tools for mundane chores coding in Android.
Terribly written in Python (no shame - this is what I use python for)


=====
View Finder Code (findViewById) Generator given XML
=====


```
python android_extract_views.py [relative or absolute path to project directory]
i.e. python android_extract_views.py Story-Quilt/
```
Outputs a .java file in the directory the python script is located in, containing the code you would normally use in android.


=====
Duplicate View IDs finder
=====


```
python dup_ids_filter.py [relative or absolute path to res directory]
i.e. python dup_ids_filter.py res/
```
Prints duplicate IDs found with path to file.


=====
Hardcoded XML views converter to Styles
=====


```
python XMLtoStyle.py [relative or absolute path to XML tag containing file]
i.e. python XMLtoStyle.py input.xml
```
Creates styles from hard-coded XMLs.

i.e.

```
        <TextView
            android:layout_width="match_parent"
            android:layout_height="@dimen/divider"
            android:background="@color/divider"/>
```
to 

```
        <style name="" parent="@android:style/Widget.TextView">
        	<item name="android:layout_width">match_parent</item>
        	<item name="android:layout_height">@dimen/divider</item>
        	<item name="android:background">@color/divider</item>
        </style>
```


It will output the style generated in output.xml of same directory as script.
