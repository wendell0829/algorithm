Use this folder to store your figures (e.g. PNG or JPG files).
Upload the PNG or JPG file to this folder, and then use the following code to use it in your document:

\begin{figure}
    \centering
    \includegraphics[width=0.8\linewidth]{figures\some_file.png}
    \caption{Caption}
    \label{fig:my_label}
\end{figure}

The option [width=0.8\linewidth] sets the width to 80% of the line width of the page.