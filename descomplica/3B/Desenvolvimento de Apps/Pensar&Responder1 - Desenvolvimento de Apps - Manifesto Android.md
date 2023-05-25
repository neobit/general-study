activity_main.xml:
```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
   xmlns:tools="http://schemas.android.com/tools"
   android:layout_width="match_parent"
   android:layout_height="match_parent"
   android:gravity="center"
   android:orientation="vertical"
   tools:context=".MainActivity">

   <TextView
       android:id="@+id/nomeTextView"
       android:layout_width="wrap_content"
       android:layout_height="wrap_content"
       android:text="Josecrilson Limeira Ramos"/>

   <TextView
       android:id="@+id/cursoTextView"
       android:layout_width="wrap_content"
       android:layout_height="wrap_content"
       android:text="Jogos Digitais"/>

   <TextView
       android:id="@+id/faculdadeTextView"
       android:layout_width="wrap_content"
       android:layout_height="wrap_content"
       android:text="Faculdade UniAmérica Descomplica"/>

</LinearLayout>
```
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
No código acima, não esquecer de alterar para o seu nome^.

MainActivity.java:

```java
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

   @Override
   protected void onCreate(Bundle savedInstanceState) {
       super.onCreate(savedInstanceState);
       setContentView(R.layout.activity_main);
   }
}
```