package com.dhakreystock.ai;

import android.app.AlarmManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.os.Build;
import android.os.Bundle;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {

    private static final String PREFS_NAME = "DhakreyStockPrefs";
    private static final int PERMISSION_REQUEST_CODE = 101;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Request Notification permission for Android 13+ (API 33+)
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
            if (ContextCompat.checkSelfPermission(this, android.Manifest.permission.POST_NOTIFICATIONS)
                    != PackageManager.PERMISSION_GRANTED) {
                ActivityCompat.requestPermissions(
                    this,
                    new String[]{android.Manifest.permission.POST_NOTIFICATIONS},
                    PERMISSION_REQUEST_CODE
                );
            }
        }

        // Schedule user engagement reminder (2.5 to 3 hours from open)
        scheduleEngagementNotification();
    }

    private void scheduleEngagementNotification() {
        try {
            SharedPreferences prefs = getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE);
            long lastScheduledTime = prefs.getLong("last_scheduled_timestamp", 0);
            long now = System.currentTimeMillis();

            // Reschedule if at least 2 hours have passed since last scheduling
            if (now - lastScheduledTime > (2 * 60 * 60 * 1000)) {
                AlarmManager alarmManager = (AlarmManager) getSystemService(Context.ALARM_SERVICE);
                if (alarmManager != null) {
                    Intent intent = new Intent(this, EngagementNotificationReceiver.class);
                    int flags = PendingIntent.FLAG_UPDATE_CURRENT;
                    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
                        flags |= PendingIntent.FLAG_IMMUTABLE;
                    }
                    PendingIntent pendingIntent = PendingIntent.getBroadcast(this, 100, intent, flags);

                    // Trigger ~2.5 - 3 hours (2 hours 45 minutes = 9,900,000 ms)
                    long triggerAtMillis = now + (long) (2.75 * 60 * 60 * 1000);

                    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
                        alarmManager.setAndAllowWhileIdle(AlarmManager.RTC_WAKEUP, triggerAtMillis, pendingIntent);
                    } else {
                        alarmManager.set(AlarmManager.RTC_WAKEUP, triggerAtMillis, pendingIntent);
                    }

                    prefs.edit().putLong("last_scheduled_timestamp", now).apply();
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
