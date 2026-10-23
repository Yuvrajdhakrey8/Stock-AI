package com.dhakreystock.ai;

import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Build;
import androidx.core.app.NotificationCompat;

public class EngagementNotificationReceiver extends BroadcastReceiver {
    public static final String CHANNEL_ID = "dhakreystock_engagement";
    public static final int NOTIFICATION_ID = 1001;

    @Override
    public void onReceive(Context context, Intent intent) {
        NotificationManager notificationManager = (NotificationManager) context.getSystemService(Context.NOTIFICATION_SERVICE);
        if (notificationManager == null) return;

        // Create Channel for Android 8.0+ (Oreo and above)
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            NotificationChannel channel = new NotificationChannel(
                CHANNEL_ID,
                "Market & IPO Reminders",
                NotificationManager.IMPORTANCE_DEFAULT
            );
            channel.setDescription("Timely market updates, trending stocks, and live IPO GMP alerts");
            notificationManager.createNotificationChannel(channel);
        }

        // Tap action -> Open App (MainActivity)
        Intent launchIntent = new Intent(context, MainActivity.class);
        launchIntent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TOP);
        int pendingFlags = PendingIntent.FLAG_UPDATE_CURRENT;
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            pendingFlags |= PendingIntent.FLAG_IMMUTABLE;
        }
        PendingIntent pendingIntent = PendingIntent.getActivity(
            context,
            0,
            launchIntent,
            pendingFlags
        );

        String[] titles = {
            "📈 Aaj Ka Market & IPO GMP Check Kiya?",
            "⚡ Trending Stocks & Valuation Alerts",
            "🚀 Live IPO Allotment & Grey Market Check"
        };
        String[] bodies = {
            "Check live IPO GMP, subscription status and top breakout stocks now on DhakreyStock AI!",
            "Explore Fair Value & Graham Number for top Indian companies before market moves.",
            "Verify your IPO allotment status and see which sectors are trending today."
        };

        int randomIndex = (int) (Math.random() * titles.length);

        NotificationCompat.Builder builder = new NotificationCompat.Builder(context, CHANNEL_ID)
            .setSmallIcon(R.mipmap.ic_launcher)
            .setContentTitle(titles[randomIndex])
            .setContentText(bodies[randomIndex])
            .setStyle(new NotificationCompat.BigTextStyle().bigText(bodies[randomIndex]))
            .setPriority(NotificationCompat.PRIORITY_DEFAULT)
            .setContentIntent(pendingIntent)
            .setAutoCancel(true);

        notificationManager.notify(NOTIFICATION_ID, builder.build());
    }
}
