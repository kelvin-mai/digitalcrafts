let articles = [
  {
    title:'Hello WatchKit',
    link: '/Articles/880_Hello_WatchKit.aspx',
    post: 'Last month Apple released the anticipated WatchKit Framework for developers in the form of iOS 8.2 beta SDK release. The WatchKit framework enable the developers to create Apple Watch applications. In this article we are going to focus on the basics of getting started with the WatchKit framework and developing apps for the Apple Watch.',
    comments: 12,
    likes: 124
  }, {
    title: 'Introduction to Swift',
    link: '/Articles/879_Introduction_to_Swift.aspx',
    post: 'Swift is a modern programming language developed by Apple to create the next generation of iOS and OSX applications. Swift is a fairly new language and still in development but it clearly reflects the intentions and the future direction. This article will revolve around the basic concepts in the Swift language and how you can get started.',
    comments: 9,
    likes: 104
  }, {
    title: 'Creating Gravity Enabled Notification Banner Control in iOS 7',
    link: '/Articles/878_Creating_Gravity_Enabled_Notification_Banner_Control_in_iOS_7.aspx',
    post: 'iOS 7 framework introduced many new features which allowed the developers to create the next generation of applications. One of the most interesting feature is UIKit Dynamics framework. UIKit Dynamics allows the developer to create physics enabled effects which users can relate to the real world. In this article we are going to implement a notification banner control which utilizes the features provided by the UIKit Dynamics framework. ',
    comments: 13,
    likes:174
  }, {
    title: 'Tilt Scrolling Using Core Motion',
    link: '/Articles/877_Tilt_Scrolling_Using_Core_Motion.aspx',
    post: 'The tilt to scroll functionality has become an integral part of any text heavy application. The first time we got introduced to the tilt to scroll functionality was through the Instapaper application. In this article we will demonstrate how to implement this functionality using Core Motion API. ',
    comments: 21,
    likes: 213
  }, {
    title: 'Creating a Flipping Tweets View',
    link: '/Articles/876_Creating_a_Flipping_Tweets_View.aspx',
    post: 'he number of ways that you can display a Twitter feed in your app is only limited by your imagination. In this article we will demonstrate how you can implement a flipping view which displays the tweets inside your app.',
    comments: 43,
    likes: 724
  }
]

$('#container').addClass('container');


let hero = $('<div/>').addClass('container').prependTo($('body'));
hero = $('<div/>').addClass('hero').appendTo(hero);
$('<h1/>').appendTo(hero).text('The Curse of the Current Reviews');
$('<p/>').appendTo(hero).text('When you want to buy any application from the Apple iTunes store you have more choices than you can handle. Most of the users scroll past the application description completely avoiding it like ads displayed on the right column of your webpage. Their choice is dependent on three important factors price, screenshot and reviews.');
$('<a>Read More</a>').attr('href',"/Articles/881_The_Curse_of_the_Current_Reviews.aspx").appendTo(
    $('<p/>').appendTo(hero)
  );

let header = $('<div/>').addClass('header').prependTo($('body'));
header = $('<div/>').addClass('container').appendTo(header);
$('<h1>HighOnCoding</h1>').addClass('header_logo').appendTo(header);
let nav = $('<ul/>').addClass('nav').appendTo(header);
$('<li><a href="index.html">Home</a><li>').addClass('nav_button nav_button-active').appendTo(nav);
$('<li><a href="categories.html">Categories</a></li>').addClass('nav_button').appendTo(nav);

articles.forEach(function(article){
  let post = $('<div/>').addClass('post').appendTo($('#container')); $('<a/>').addClass('post_title').appendTo(post).attr('href',article.link).text(article.title);
  $('<p/>').appendTo(post).text(article.post);
  let response = $('<ul/>').addClass('post_response').appendTo(post);
  $('<li/>').appendTo(response).text(article.comments + ' comments');
  $('<li/>').appendTo(response).text(article.likes + ' likes');
});
