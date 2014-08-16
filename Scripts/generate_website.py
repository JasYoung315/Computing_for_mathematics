#! /usr/bin/env python

import os

# Open index file

index_file = open("../index.md", "w")
index_file.write("""

<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>Fair Individual Marks</title>
<meta name="viewport" content="width=device-width">
<link rel="icon" href="./favicon.ico" type="image/x-icon" />
<link rel="stylesheet" href="main.css">

<script>
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-38016329-2', 'auto');
ga('send', 'pageview');

</script>

</head>
<header class="site-header">

<div class="wrap">

<a class="site-title" href="./index.html">Fair Individual Marks</a>

<nav class="site-nav">
<a href="#" class="menu-icon">
 <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
    viewBox="0 0 18 15" enable-background="new 0 0 18 15" xml:space="preserve">
   <path fill="#505050" d="M18,1.484c0,0.82-0.665,1.484-1.484,1.484H1.484C0.665,2.969,0,2.304,0,1.484l0,0C0,0.665,0.665,0,1.484,0
     h15.031C17.335,0,18,0.665,18,1.484L18,1.484z"/>
   <path fill="#505050" d="M18,7.516C18,8.335,17.335,9,16.516,9H1.484C0.665,9,0,8.335,0,7.516l0,0c0-0.82,0.665-1.484,1.484-1.484
     h15.031C17.335,6.031,18,6.696,18,7.516L18,7.516z"/>
   <path fill="#505050" d="M18,13.516C18,14.335,17.335,15,16.516,15H1.484C0.665,15,0,14.335,0,13.516l0,0
     c0-0.82,0.665-1.484,1.484-1.484h15.031C17.335,12.031,18,12.696,18,13.516L18,13.516z"/>
 </svg>
</a>
<div class="trigger">
  <a class="page-link" href="drvinceknight.github.io/">Personal Site</a>
  <a class="page-link" href="drvinceknight.github.io/unpeudemath">Blog</a>
  <a class="page-link" href="drvinceknight.github.io/teaching">Teaching</a>
  <a class="page-link" href="drvinceknight.github.io/research">Research</a>
  <a class="page-link" href="drvinceknight.github.io/outreach">Outreach</a>
  <a class="page-link" href="drvinceknight.github.io/other">Other</a>
</div>
</nav>

</div>
</header>

<body>
<div class="page-content">
<div class="wrap">
<div class="home"> """)
index_file.write("# Computing for mathematics")
index_file.write("\n")

# Notes

index_file.write("""
This website contains the lab sheets for the first term of Computing for Mathematics. Each lab sheet contains links to a number of videos that should help with the exercises.
                 """)
index_file.write("\n")

# Write course notes

target_dir = "../LabSheets"

list_of_lab_sheets = os.listdir(target_dir)
list_of_md_sheets = [p for p in list_of_lab_sheets if p[-3:] == ".md"]
list_of_md_sheets.sort()
number_of_lab_sheets = len(list_of_md_sheets)
print "%s lab sheets read." % number_of_lab_sheets

index_file.write("\n")
index_file.write("\n## Lab Sheets")
index_file.write("\n")

for i in range(len(list_of_md_sheets)):
    outfile = open(target_dir + "/" + list_of_md_sheets[i])
    data = outfile.read().split("\n")
    outfile.close()
    file_name = list_of_md_sheets[i][:-3]
    index_file.write("\n%s. Lab Sheets %s: %s" % (i + 1, i + 1, data[0][data[0].index("-") + 2:]))
    index_file.write("\n")
    index_file.write("\n\t[html (recommended)](./LabSheets/%s.html), [pdf](./LabSheets/%s.pdf), [docx](./LabSheets/%s.docx)" % (file_name, file_name, file_name))
    index_file.write("\n")

# Write handout

target_dir = "../Handouts"

list_of_handouts = os.listdir(target_dir)
list_of_md_sheets = [p for p in list_of_handouts if p[-3:] == ".md"]
list_of_md_sheets.sort()
number_of_lab_sheets = len(list_of_md_sheets)
print "%s handouts read." % number_of_lab_sheets

index_file.write("\n")
index_file.write("\n## Handouts")
index_file.write("\n")

for i in range(len(list_of_md_sheets)):
    outfile = open(target_dir + "/" + list_of_md_sheets[i])
    data = outfile.read().split("\n")
    outfile.close()
    file_name = list_of_md_sheets[i][:-3]
    index_file.write("\n%s. Handout %s: %s" % (i + 1, i + 1, data[0][data[0].index("-") + 2:]))
    index_file.write("\n")
    index_file.write("\n\t[html (recommended)](./Handouts/%s.html), [pdf](./Handouts/%s.pdf), [docx](./Handouts/%s.docx)" % (file_name, file_name, file_name))
    index_file.write("\n")
# Write Lesson plans

#target_dir = "../Lesson_Plans"
#index_file.write("\n## Lesson plans")
#
#list_of_plans = os.listdir(target_dir)
#list_of_plans = [p for p in list_of_plans if p[-3:] == ".md"]
#list_of_plans.sort()
#number_of_plans = len(list_of_plans)
#print "%s lesson plans read." % number_of_plans
#
#for i in range(len(list_of_plans)):
#    outfile = open(target_dir + "/" + list_of_plans[i])
#    data = outfile.read().split("\n")
#    outfile.close()
#
#    index_file.write("\n%s. Week %s: [%s](./Lesson_Plans/Week_%.02d.html)" % (i + 1, i + 1, data[1][2:], i + 1))
#
#index_file.write("\n")
#
#
#index_file.write("""

### Reading List

index_file.write("""
Alternative resources can be found [here](./alternativeresources.html).

[My personal website](http://www.vincent-knight.com/) contains information with regards to assessment and also solutions to the lab sheets.

<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-38016329-2']);
  _gaq.push(['_setDomainName', 'github.com']);
  _gaq.push(['_setAllowLinker', true]);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
                 """)


index_file.write("""
</div>
</div>
</div>
<footer class="site-footer">

<div class="wrap">

<h2 class="footer-heading">Vince Knight</h2>

<div class="footer-col-1 column">
  <ul>
    <li>
      <a href="https://github.com/drvinceknight">
        <span class="icon github">
          <svg version="1.1" class="github-icon-svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
             viewBox="0 0 16 16" enable-background="new 0 0 16 16" xml:space="preserve">
            <path fill-rule="evenodd" clip-rule="evenodd" fill="#C2C2C2" d="M7.999,0.431c-4.285,0-7.76,3.474-7.76,7.761
            c0,3.428,2.223,6.337,5.307,7.363c0.388,0.071,0.53-0.168,0.53-0.374c0-0.184-0.007-0.672-0.01-1.32
            c-2.159,0.469-2.614-1.04-2.614-1.04c-0.353-0.896-0.862-1.135-0.862-1.135c-0.705-0.481,0.053-0.472,0.053-0.472
            c0.779,0.055,1.189,0.8,1.189,0.8c0.692,1.186,1.816,0.843,2.258,0.645c0.071-0.502,0.271-0.843,0.493-1.037
            C4.86,11.425,3.049,10.76,3.049,7.786c0-0.847,0.302-1.54,0.799-2.082C3.768,5.507,3.501,4.718,3.924,3.65
            c0,0,0.652-0.209,2.134,0.796C6.677,4.273,7.34,4.187,8,4.184c0.659,0.003,1.323,0.089,1.943,0.261
            c1.482-1.004,2.132-0.796,2.132-0.796c0.423,1.068,0.157,1.857,0.077,2.054c0.497,0.542,0.798,1.235,0.798,2.082
            c0,2.981-1.814,3.637-3.543,3.829c0.279,0.24,0.527,0.713,0.527,1.437c0,1.037-0.01,1.874-0.01,2.129
            c0,0.208,0.14,0.449,0.534,0.373c3.081-1.028,5.302-3.935,5.302-7.362C15.76,3.906,12.285,0.431,7.999,0.431z"/>
          </svg>
        </span>
        <span class="username">drvinceknight</span>
      </a>
    </li>
    <li>
      <a href="https://twitter.com/@drvinceknight">
        <span class="icon twitter">
          <svg version="1.1" class="twitter-icon-svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
             viewBox="0 0 16 16" enable-background="new 0 0 16 16" xml:space="preserve">
            <path fill="#C2C2C2" d="M15.969,3.058c-0.586,0.26-1.217,0.436-1.878,0.515c0.675-0.405,1.194-1.045,1.438-1.809
            c-0.632,0.375-1.332,0.647-2.076,0.793c-0.596-0.636-1.446-1.033-2.387-1.033c-1.806,0-3.27,1.464-3.27,3.27
            c0,0.256,0.029,0.506,0.085,0.745C5.163,5.404,2.753,4.102,1.14,2.124C0.859,2.607,0.698,3.168,0.698,3.767
            c0,1.134,0.577,2.135,1.455,2.722C1.616,6.472,1.112,6.325,0.671,6.08c0,0.014,0,0.027,0,0.041c0,1.584,1.127,2.906,2.623,3.206
            C3.02,9.402,2.731,9.442,2.433,9.442c-0.211,0-0.416-0.021-0.615-0.059c0.416,1.299,1.624,2.245,3.055,2.271
            c-1.119,0.877-2.529,1.4-4.061,1.4c-0.264,0-0.524-0.015-0.78-0.046c1.447,0.928,3.166,1.469,5.013,1.469
            c6.015,0,9.304-4.983,9.304-9.304c0-0.142-0.003-0.283-0.009-0.423C14.976,4.29,15.531,3.714,15.969,3.058z"/>
          </svg>
        </span>
        <span class="username">@drvinceknight</span>
      </a>
    </li>
    <li>
      <a href="https://plus.google.com/+VincentKnight">
        <span class="icon G+">
            <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                 width="16px" height="16px" viewBox="0 0 134.658 131.646" enable-background="new 0 0 134.658 131.646"
                 xml:space="preserve">
            <g>
                <path fill="#C2C2C2" d="M126.515,4.109H8.144c-2.177,0-3.94,1.763-3.94,3.938v115.546c0,2.179,1.763,3.942,3.94,3.942h118.371
                    c2.177,0,3.94-1.764,3.94-3.942V8.048C130.455,5.872,128.691,4.109,126.515,4.109z"/>
                <g>
                    <path fill="#FFFFFF" d="M70.479,71.845l-3.983-3.093c-1.213-1.006-2.872-2.334-2.872-4.765c0-2.441,1.659-3.993,3.099-5.43
                        c4.64-3.652,9.276-7.539,9.276-15.73c0-8.423-5.3-12.854-7.84-14.956h6.849l7.189-4.517H60.418
                        c-5.976,0-14.588,1.414-20.893,6.619c-4.752,4.1-7.07,9.753-7.07,14.842c0,8.639,6.633,17.396,18.346,17.396
                        c1.106,0,2.316-0.109,3.534-0.222c-0.547,1.331-1.1,2.439-1.1,4.32c0,3.431,1.763,5.535,3.317,7.528
                        c-4.977,0.342-14.268,0.893-21.117,5.103c-6.523,3.879-8.508,9.525-8.508,13.51c0,8.202,7.731,15.842,23.762,15.842
                        c19.01,0,29.074-10.519,29.074-20.932C79.764,79.709,75.344,75.943,70.479,71.845z M56,59.107
                        c-9.51,0-13.818-12.294-13.818-19.712c0-2.888,0.547-5.87,2.428-8.199c1.773-2.218,4.861-3.657,7.744-3.657
                        c9.168,0,13.923,12.404,13.923,20.382c0,1.996-0.22,5.533-2.762,8.09C61.737,57.785,58.762,59.107,56,59.107z M56.109,103.65
                        c-11.826,0-19.452-5.657-19.452-13.523c0-7.864,7.071-10.524,9.504-11.405c4.64-1.561,10.611-1.779,11.607-1.779
                        c1.105,0,1.658,0,2.538,0.111c8.407,5.983,12.056,8.965,12.056,14.629C72.362,98.542,66.723,103.65,56.109,103.65z"/>
                    <polygon fill="#FFFFFF" points="98.393,58.938 98.393,47.863 92.923,47.863 92.923,58.938 81.866,58.938 81.866,64.469
                        92.923,64.469 92.923,75.612 98.393,75.612 98.393,64.469 109.506,64.469 109.506,58.938       "/>
                </g>
            </g>
            </svg>
        </span>
        <span class="username">+VincentKnight</span>
      </a>
    </li>
  </ul>
</div>

<div class="footer-col-2 column">
  <p class="text">This site contains information about a methodology used to calculate fair individual marks in a group project using game theory.</p>
</div>

</div>

</footer>
</body>
""")
index_file.close()

os.system("pandoc ../index.md -o ../index.html")
