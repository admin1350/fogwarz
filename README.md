# fogwarz
Вот готовый Markdown-файл, в котором собраны все шаги по настройке алертов в Grafana для CPU и памяти с отправкой в Telegram.
Вы можете скопировать этот текст и сохранить его как grafana_alerts.md.
Настройка уведомлений Grafana в Telegram
В этом руководстве описан процесс создания Telegram-бота, настройки точки контакта и создания правил оповещения для CPU и оперативной памяти.
1. Подготовка Telegram-бота
Найдите в Telegram бота @BotFather и создайте нового бота командой /newbot. Сохраните полученный API Token.
Создайте группу, добавьте туда бота и получите Chat ID (с помощью бота @getidsbot).
Обязательно напишите что-нибудь в группу, чтобы активировать чат для бота.
2. Настройка Contact Point в Grafana
Для того чтобы Grafana знала, куда отправлять сообщения:
Перейдите в Alerting > Contact points.
Нажмите + Add contact point.
Name: tel (или любое другое).
Integration: Telegram.
BOT API Token: вставьте ваш токен.
Chat ID: вставьте ваш ID (например, 1181667933).
Parse Mode: установите HTML.
Нажмите Test, чтобы убедиться, что сообщение пришло в Telegram, и затем Save.
3. Создание правила для CPU
Чтобы отслеживать нагрузку на процессор:
Шаг 1: Запрос (Query A)
Используйте формулу для Prometheus (тип Range):
promql
100 - (avg by (instance) (irate(node_cpu_seconds_total{instance="10.31.0.122:9100", mode="idle"}[5m])) * 100)
Используйте код с осторожностью.

Шаг 2: Обработка (Expression B - Reduce)
Input: A
Function: Last (берет последнее значение).
Шаг 3: Порог (Expression C - Threshold)
Input: B
Condition: IS ABOVE 85 (уведомлять, если нагрузка > 85%).
Важно: Нажмите кнопку Set as alert condition (иконка станет синей) именно на этом блоке.
Шаг 4: Описание (Annotations)
Добавьте аннотацию description, чтобы сообщение было информативным:
Нагрузка на процессор ({{ $labels.instance }}) составляет {{ $values.B.Value | printf "%.2f" }}%
4. Создание правила для памяти (RAM)
Если нужно отслеживать потребление оперативной памяти:
Шаг 1: Запрос (Query A)
promql
clamp_min((1 - (node_memory_MemAvailable_bytes{instance="10.31.0.122:9100"} / node_memory_MemTotal_bytes{instance="10.31.0.122:9100"})) * 100, 0)
Используйте код с осторожностью.

Установите тип Range.
Шаг 2 и 3:
Настройте блоки Reduce и Threshold аналогично правилу для CPU (порог 85).
5. Кастомный шаблон сообщения (Notification Template)
Если вы хотите изменить внешний вид стандартного сообщения, перейдите в Contact points > Notification templates и добавьте шаблон:
go
{{ define "telegram.message" }}
  {{ if gt (len .Alerts.Firing) 0 }}
    🔥 <b>ОБНАРУЖЕНЫ ПРОБЛЕМЫ</b>
    {{ range .Alerts.Firing }}
      📌 <b>Алерт:</b> {{ .Labels.alertname }}
      🖥 <b>Хост:</b> {{ .Labels.instance }}
      📈 <b>Значение:</b> {{ .ValueString }}
    {{ end }}
  {{ end }}
{{ end }}
Используйте код с осторожностью.

Затем в настройках Contact Point в поле Message пропишите: {{ template "telegram.message" . }}.
Частые ошибки
Статус Firing постоянно: Проверьте, установлена ли синяя галочка "Alert condition" на блоке Threshold, а не на блоке Query.
Сообщения не приходят: Проверьте Alerting > Notification policies. В поле Default policy должен быть выбран ваш контакт tel.
Нужно ли добавить в файл инструкции по установке node_exporter, если данные перестанут поступать?



