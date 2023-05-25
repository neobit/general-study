Activity 1:

```java
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        findViewById(R.id.btn_activity2).setOnClickListener(v -> startActivity(new Intent(this, Activity2.class)));
    }
}
```


Layout para Activity 1 (activity_main.xml):
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:gravity="center"
    android:orientation="vertical">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Activity 1" />

    <Button
        android:id="@+id/btn_activity2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Go to Activity 2" />
</LinearLayout>
```

Activity 2:
```java
public class Activity2 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_2);

        findViewById(R.id.btn_activity3).setOnClickListener(v -> startActivity(new Intent(this, Activity3.class)));
    }
}
```

Layout para Activity 2 (activity_2.xml):
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:gravity="center"
    android:orientation="vertical">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Activity 2" />

    <Button
        android:id="@+id/btn_activity3"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Go to Activity 3" />
</LinearLayout>
```

Activity 3:
```java
public class Activity3 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_3);

        findViewById(R.id.btn_activity1).setOnClickListener(v -> startActivity(new Intent(this, MainActivity.class)));
    }
}
```

Layout para Activity 3 (activity_3.xml):
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:gravity="center"
    android:orientation="vertical">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Activity 3" />

    <Button
        android:id="@+id/btn_activity1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Go to Activity 1" />
</LinearLayout>
```