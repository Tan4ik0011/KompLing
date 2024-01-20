<h1 align="center">Компьютерная лингвистика.</h1>
<h1 align="center">Контрольная работа. Вариант  <a href="https://gorvesti.ru/">№5</a></h1>
<hr>
<h2>Задание №1: Распарсить сайт из списка согласно номеру задания. Краулер должен считывать новостную ленту с первой страницы сайта или из rss-ленты. Периодичность повторения парсинга устанавливается пользователем.</h2>
<ul>
  <li>Данные заполняются в БД (не менее 10 тыс. новостей). Обязательные распарсенные поля для текста новости:</li>
  <li>Название новости</li>
  <li>Дата новости</li>
  <li>Ссылка на новость</li>
  <li>Текст новости</li>
  <li>Данная информация отображается в разработанном чат-боте для Telegram. Новости появляются в конце списка согласно дате публикации на сайте (самые новые - последние).</li>
</ul>
<hr>
<h2>Задание №2: Выявить с помощью Томита-парсера упоминание в тексте vip-персон Волгоградской области и достопримечательностей.</h2>
<ul>
  <li>Дополнить информацию о новости в чат-боте Telegram следующими полями:</li>
  <li><a href="https://мтв.онлайн/feed/obshchestvo/andrey-bocharov-vozglavil-top-100-vliyatelnykh-lyudey-volgogradskoy-oblasti-7478520448.html">VIP-персоны</a></li>
  <li><a href="https://www.kp.ru/russia/volgograd/dostoprimechatelnosti/">Достопримечательности</a></li>
  <li>С помощью Spark MlLib и модели word2vec провести анализ на всем объеме новостных статей из БД. Для любого введенного слова определить контекстные синонимы и слова, с которыми они упоминались в тексте.</li>
</ul>
<hr>
<h2>Задание №3: Подключить <a href="https://developers.sber.ru/portal/products/summarizer">Суммаризатор</a> для создания аннотации новости. Подключить <a href="https://developers.sber.ru/portal/products/rewriter">Рерайтер</a> для переписывания текста новости</h2>
<ul>
  <li>Осуществить выявление тональности высказываний по отношению к текстам новостей с упоминанием vip-персон Волгоградской области и достопримечательностей.</li>
  <li>Дополнить информацию о новости в чат-боте Telegram следующими полями:</li>
  <li>Аннотация</li>
  <li>Переписанная новость</li>
  <li>Оценка тональности новости</li>
</ul>
<hr>
<h2><a href="">Бот</a>, содержащий базу данных из новостей с сайта <a href="https://gorvesti.ru/">Горвести</a></h2>
<hr>
<h2>Весь текст обработан с помощью лингвистических инструментов</h2>
<hr>
<h2>Стек технологий</h2>
<h3>Инструменты:</h3>
<ul>
  <li><i>ЯП: Python 3.12.0</i></li>
  <li><i>БД: Yandex cloud </i></li>
  <li><i>Интрефейс: Telegram Bot</i></li>
  <li><i>Среда разработки: Visual Studio Code</i></li>
  <li><i>Фреймворк Apache Spark 3.5.0</i></li>
</ul>
<h3>Библиотеки</h3>
<ul>
  <li><i>aiohttp</i></li>
  <li><i>asyncio</i></li>
  <li><i>bs4</i></li>
  <li><i>pytelegrambotapi</i></li>
  <li><i>gigachat</i></li>
  <li><i>nltk</i></li>
  <li><i>pyspark</i></li>
  <li><i>apscheduler</i></li>
</ul>
<hr>
 <h2 align="center">Команда</h2>
 <h2 align="center">> Лопанцев Дмитрий Сергеевич ИВТ-360 (Задание №1)</h2>
 <h2 align="center"><a href="https://github.com/Tan4ik0011"><img src="https://avatars.githubusercontent.com/u/93055785?s=400&v=4"></a></h2>
 <h2 align="center">> Батырев Вадим ИВТ-360 (Задание №2)</h2>
<h2 align = "center" style = "width:50 px; height: 50 px"><a href="" ><img src=""></a></h2>
 <h2 align="center">> Сердюкова Александра ИВТ-360 (Задание №3)</h2>
 <h2 align = "center" style = "width:50 px; height: 50 px"><a href=""><img src=""></a></h2>
