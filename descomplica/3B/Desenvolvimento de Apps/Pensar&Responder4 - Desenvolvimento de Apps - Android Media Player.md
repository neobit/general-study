Código Java (MainActivity.java):

package com.example.mediaplayer;

import androidx.appcompat.app.AppCompatActivity;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {
    private MediaPlayer mediaPlayer;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Inicializando MediaPlayer com a música da pasta raw
        mediaPlayer = MediaPlayer.create(this, R.raw.minha_musica);

        Button startButton = findViewById(R.id.start_button);
        Button pauseButton = findViewById(R.id.pause_button);
        Button stopButton = findViewById(R.id.stop_button);

        // Configurando o botão Start para tocar a música
        startButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mediaPlayer.start();
            }
        });

        // Configurando o botão Pause para pausar a música
        pauseButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(mediaPlayer.isPlaying()){
                    mediaPlayer.pause();
                }
            }
        });

        // Configurando o botão Stop para parar a música
        stopButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(mediaPlayer.isPlaying()){
                    mediaPlayer.stop();
                    // Necessário recriar o MediaPlayer após o stop()
                    mediaPlayer = MediaPlayer.create(getApplicationContext(), R.raw.minha_musica);
                }
            }
        });
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        // Libera os recursos do MediaPlayer quando a atividade é destruída
        if (mediaPlayer != null) {
            mediaPlayer.release();
        }
    }
}

Código XML (activity_main.xml):

<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <Button
        android:id="@+id/start_button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Start"
        android:layout_centerHorizontal="true"
        android:layout_marginTop="150dp"/>

    <Button
        android:id="@+id/pause_button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Pause"
        android:layout_below="@+id/start_button"
        android:layout_centerHorizontal="true"
        android:layout_marginTop="50dp"/>

    <Button
        android:id="@+id/stop_button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Stop"
        android:layout_below="@+id/pause_button"
        android:layout_centerHorizontal="true"
        android:layout_marginTop="50dp"/>

</RelativeLayout>

Na classe MainActivity, no método onCreate(), inicializamos o MediaPlayer com a música da pasta "raw" utilizando MediaPlayer.create(). Em seguida, associamos os botões do layout XML aos objetos Button no código Java.

O botão Start inicia a reprodução da música quando clicado, utilizando mediaPlayer.start(). O botão Pause pausa a reprodução caso a música esteja tocando, utilizando mediaPlayer.pause(). O botão Stop interrompe a reprodução e reinicia o MediaPlayer para que a música possa ser tocada novamente desde o início.

No método onDestroy(), liberamos os recursos do MediaPlayer chamando mediaPlayer.release().