<?xml version="1.0" encoding="utf-8"?> 
<androidx.constraintlayout.widget.ConstraintLayout 
    xmlns:android="http://schemas.android.com/apk/res/android" 
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent" tools:context=".MainActivity">

    <EditText
        android:id="@+id/editText_PhoneNumber"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_marginStart="16dp"
        android:layout_marginEnd="16dp"
        android:hint="Insira o Número"
        android:inputType="phone"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent"/>

    <EditText
        android:id="@+id/editText_Message"
        android:layout_width="0dp"
        android:layout_height="0dp"
        android:layout_marginTop="16dp"
        android:layout_marginStart="16dp"
        android:layout_marginEnd="16dp"
        android:hint="Insira a Mensagem"
        android:inputType="textMultiline"
        app:layout_constraintBottom_toTopOf="@id/button_SendMsg"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@id/editText_PhoneNumber"/>

    <Button
        android:id="@+id/button_SendMsg"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_marginStart="16dp"
        android:layout_marginEnd="16dp"
        android:layout_marginBottom="16dp"
        android:text="Enviar Mensagem"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"/>

</androidx.constraintlayout.widget.ConstraintLayout>

package com.example.sms;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.telephony.SmsManager;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    Button buttonSendMsg;
    EditText editTextPhoneNumber, editTextMessage;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        buttonSendMsg = findViewById(R.id.button_SendMsg);
        editTextPhoneNumber = findViewById(R.id.editText_PhoneNumber);
        editTextMessage = findViewById(R.id.editText_Message);

        buttonSendMsg.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String phoneNumber = editTextPhoneNumber.getText().toString(); 
                String messageText = editTextMessage.getText().toString();

                if (!phoneNumber.isEmpty() && !messageText.isEmpty()) {
                    try {
                        SmsManager sms = SmsManager.getDefault();
                        sms.sendTextMessage(phoneNumber, null, messageText, null, null);
                        Toast.makeText(MainActivity.this, "SMS Enviado", Toast.LENGTH_SHORT).show();
                    } catch (Exception e) {
                        Toast.makeText(MainActivity.this, "Erro ao enviar SMS", Toast.LENGTH_SHORT).show(); 
                        e.printStackTrace();
                    }
                } else {
                    Toast.makeText(MainActivity.this, "Número de telefone ou mensagem não pode estar vazio", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}

<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.sms">
    <uses-permission android:name="android.permission.SEND_SMS"/> 

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher" 
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRt1="true" 
        android:theme="@style/Theme.Sms">
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>