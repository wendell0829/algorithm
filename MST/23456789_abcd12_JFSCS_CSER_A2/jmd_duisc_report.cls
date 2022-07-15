% Custom Exam Class for StudyGroup/DUISC/STEM/REPORTS
% (c) Jeff Davidson, 2019-10-24

% DO NOT ALTER THE CONTENTS OF THIS FILE

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{jmd_duisc_report.cls}[2020-10-28 DUISC/STEM custom report class]

\newif\iftmfont
\tmfontfalse

\DeclareOption{tm}{\tmfonttrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax

\LoadClass[12pt, a4paper, twoside]{article}
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\iftmfont \RequirePackage{mathptmx} \fi 
\RequirePackage{lipsum}


% PACKAGES TO SET PAGE SIZE AND STYLE
\RequirePackage[inner=2cm,outer=2cm,top=2.1cm,bottom=2.1cm,bindingoffset=0.5cm]{geometry}
\RequirePackage{pdflscape} % allows individual pages to be landscape
\RequirePackage{titling} % allows custom title block
\RequirePackage{fancyhdr} % allows custom headers and footers
\RequirePackage{pdfpages} % allows complete pdfs to be included
\RequirePackage{appendix} % makes appendix follow different numbering style
\RequirePackage{chngcntr} % allows figures to follow appendix numbering

% CUSTOM FONT AND SECTION STYLES
%\RequirePackage{newtxtext,newtxmath} % Times New Roman for both text and equations

% PACKAGES FOR EXTRA FORMATTING FEATURES
\RequirePackage{parskip} % removes paragraph indentation and creates flexible paragraph spacing
\RequirePackage[british]{babel} % use British-stye formatting
%\RequirePackage[table]{xcolor}
\RequirePackage{color,colortbl} % allows use of colours
\RequirePackage{hyperref} % allows for active hyperlinks in PDF
\RequirePackage{verbatim}
\RequirePackage{framed}
\RequirePackage{listings}


% PARAGRAPH AND LINE SPACING
\RequirePackage{setspace}
%\singlespacing
\onehalfspacing
%\doublespacing
%\setlength{\parskip}{1.5em}
%\renewcommand{\baselinestretch}{1.5}

% CUSTOM SECTION AND SUBSECTION STYLE
\RequirePackage{titlesec}
% font and weight
\titleformat*{\section}{\normalsize\bfseries}
\titleformat*{\subsection}{\normalsize\itshape}
\titleformat*{\subsubsection}{\normalsize\itshape}
% spacing
\titlespacing\section{0pt}{12pt}{6pt}
\titlespacing\subsection{0pt}{\parskip}{6pt}
\titlespacing\subsubsection{0pt}{\parskip}{6pt}

% CUSTOM TABLE AND FIGURE CAPTION STYLES
%\RequirePackage{subfig}
\RequirePackage{subcaption}
\RequirePackage{caption}
\captionsetup[figure]{font=small,labelsep=colon}
\captionsetup[table]{font=small,labelsep=colon}
\RequirePackage{floatrow}
\floatsetup[table]{capposition=top}

% PACKAGE TO CHANGE DEFAULT FONT FOR BOTH TEXT AND EQUATIONS
%\RequirePackage{newtxtext,newtxmath}
\RequirePackage{steinmetz} % for full angle symbol in phasors using \phase{ }

% PACKAGES FOR COLUMNS, TABLES AND FIGURES
\RequirePackage{tabularx}
\RequirePackage{graphicx} % for placing figures and images
\RequirePackage{multicol} % allows multiple column environment
\RequirePackage{multirow} % allows multiple rows environment
\RequirePackage{diagbox} % allows a diagonal slash in a table cell
\RequirePackage{booktabs} % proper table rule lines: upper, mid and lower

% PACKAGES FOR EQUATIONS
\RequirePackage{mathtools}
\RequirePackage{exscale,relsize} % to allow increase size of some equations
\RequirePackage{amssymb} % used to get \therefore symbol
\RequirePackage{xfrac} % used to get small diagonal fraction
\relpenalty=10000 % prevent inline equations breaking in a paragraph, unless extreme conditions
\binoppenalty=10000 % prevent inline logical equations breaking in a paragraph, unless extreme conditions
\RequirePackage{cancel}

% PACKAGES FOR SI UNITS
\RequirePackage[binary-units]{siunitx}

% PACKAGES FOR GRAPHICS
\RequirePackage{tikz}

% TO MAKE REFERENCES APPEAR AS A NUMBERED SECTION
\RequirePackage[numbib,notlof,notlot,nottoc]{tocbibind}

% CHANGE DEFAULT FONT SIZE USED IN TABLES
\let\oldtabular\tabular
\renewcommand{\tabular}{\small \oldtabular}

% DUISC REPORT CUSTOMISATION

% custom commands to define parameters of report, for populating cover sheet and header
\newcommand{\department}[1]{\def\thedepartment{#1}}
\newcommand{\programmetitle}[1]{\def\theprogrammetitle{#1}}
\newcommand{\moduletitle}[1]{\def\themoduletitle{#1}}
\newcommand{\tutorname}[1]{\def\thetutorname{#1}}
\newcommand{\teachinggroup}[1]{\def\theteachinggroup{#1}}
\newcommand{\assignmentcode}[1]{\def\theassignmentcode{#1}}
\newcommand{\assignmenttitle}[1]{\def\theassignmenttitle{#1}}
\newcommand{\assignmentdeadline}[1]{\def\theassignmentdeadline{#1}}
\newcommand{\studentid}[1]{\def\thestudentid{#1}}
\newcommand{\studentduousername}[1]{\def\thestudentduousername{#1}}
\newcommand{\submissiondate}[1]{\def\thesubmissiondate{#1}}

% custom command to set the header and footer
\newcommand{\makepagestyles}
{
    \fancypagestyle{coverpage}
    {
        \fancyhf{}
        \renewcommand{\headrulewidth}{0pt} % remove line
        \setlength{\headheight}{2cm}
        \fancyhead[L]{\includegraphics[height=1.8cm]{cover/logo-duisc.png}} % left
    }
    
    % redefine plain style for the title page
    \fancypagestyle{plain}
    {
        \fancyhf{}% Clear header/footer
        % odd footer
        \fancyfoot[OL]{\MakeUppercase{\thedepartment}}
        \fancyfoot[OR]{\MakeUppercase{\themoduletitle}}
    
        % even footer
        \fancyfoot[EL]{\MakeUppercase{\themoduletitle}}
        \fancyfoot[ER]{\MakeUppercase{\thedepartment}}
        
        \setlength{\headheight}{15pt}
        \renewcommand{\headrulewidth}{0pt} % remove line
    }

    \fancypagestyle{default}
    {
        \fancyhf{}% Clear header/footer
    
        % odd header
        \fancyhead[OC]{\MakeUppercase{\thestudentid}} % AUTHOR
        \fancyhead[OR]{\thepage} % PAGE NUMBER ON ODD PAGE, AT LEFT
    
        % even header
        \fancyhead[EC]{\MakeUppercase{\theassignmentcode}} % ASSIGNMENT CODE
        \fancyhead[EL]{\thepage} % PAGE NUMBER ON ODD PAGE, AT LEFT
    
        % odd footer
        \fancyfoot[OL]{\MakeUppercase{\thedepartment}}
        \fancyfoot[OR]{\MakeUppercase{\themoduletitle}}
    
        % even footer
        \fancyfoot[EL]{\MakeUppercase{\themoduletitle}}
        \fancyfoot[ER]{\MakeUppercase{\thedepartment}}
        
        \setlength{\headheight}{15pt}
        \renewcommand{\headrulewidth}{0pt} % remove line
    }
}

% TO CHANGE DEFAULT ABSTRACT HEADING STYLE
\newenvironment{jmdabstract}
{
\renewcommand{\abstractname}{\flushleft\textbf{Abstract}\hfill}
\begin{abstract}
}
{\end{abstract}}


% appropriate settings for showing code: do not change
\lstdefinestyle{python-code}{
    language=Python,
    commentstyle=\color{gray},
    keywordstyle=\color{blue},
    numberstyle=\tiny\color{gray},
    stringstyle=\color{red},
    basicstyle=\footnotesize\ttfamily,
    breakatwhitespace=false,         
    breaklines=true,                 
    captionpos=t,                    
    keepspaces=true,                 
    numbers=left,                    
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2,
    frame=tb
}

\lstdefinestyle{c-code}{
    language=C,
    commentstyle=\color{gray},
    keywordstyle=\color{blue},
    numberstyle=\tiny\color{gray},
    stringstyle=\color{red},
    basicstyle=\footnotesize\ttfamily,
    breakatwhitespace=false,         
    breaklines=true,                 
    captionpos=t,                    
    keepspaces=true,                 
    numbers=left,                    
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2,
    frame=tb
}

\lstdefinestyle{octave-code}{
    language=Octave,
    commentstyle=\color{gray},
    keywordstyle=\color{blue},
    numberstyle=\tiny\color{gray},
    stringstyle=\color{red},
    basicstyle=\footnotesize\ttfamily,
    breakatwhitespace=false,         
    breaklines=true,                 
    captionpos=t,                    
    keepspaces=true,                 
    numbers=left,                    
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2,
    frame=tb
}

\lstdefinestyle{console-output}{
    basicstyle=\footnotesize\ttfamily,
    breakatwhitespace=false,         
    breaklines=true,                 
    captionpos=t,                    
    keepspaces=true,                 
    showspaces=false,
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2,
    frame=tb
}
