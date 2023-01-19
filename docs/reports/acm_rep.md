\section{Introduction}

Science owes its self-correcting nature to certain norms of research in the scientific community, including organized skepticism and communalism \cite{sociology_merton_1972}.
These norms require reproducible computational experiments.

\textbf{Organized skepticism} means that experiments can be rerun, modified, and scrutinized by scientists not connected to the authors \cite{sociology_merton_1972}.
When experiments in modern science are not reproducible, they lose important validation opportunities, and if they are wrong, they steer other scientists in the wrong direction and damage public trust in science.
Irreproducibility is big enough that X and Y proclaim there is a ``reproducibility crisis'' in modern science.
\todo{For example, alzheimers research?}
Unlike physical experiments, computational experiments have no requirement for a steady hand, calibrated sensors, or uncontaminated dishware; one would expect they should be a lot easier to reproduce.
Nevertheless, computational experiments are the source of much irreproducibility \cite{mytkowicz_producing_2009}.\todo{Cite chang's retraction}

**Undermines long-term credibility**: Computational experiments are widely used in many scientific disciplines.
More than 90% of scientists surveyed across all fields use research software and 50% develop software for their research experiments [@hettrick_softwaresavedsoftware_in_research_survey_2014_2018].
If computational experiments are allowed to collapse, scientists cannot independently verify or build on each other's results, which requires replicability.
This undermines two fundamental norms of science identified by Merton, organized skepticism and communalism [@merton_sociology_1974], that make science self-correcting.
   In recent years, this has manifested itself as the ongoing reproducibility crisis[^repeatability-crisis] in computational science [@collberg_repeatability_2016], which damages the long-term credibility of science [@ritchie_science_2020].
   
[^repeatability-crisis]:
Despite these definitions, the ``reproducibility crisis'' in computational science is primarily due to non-replicable computational experiments.
If they were at least replicable but not necessarily reproducible, independent researchers chould scrutinize or build on those results.

\textbf{Communalism} means that any scientist can freely use methods of research developed by someone else.
Without this, scientists have to duplicate each others work.


**Hinders day-to-day operations**: Consider scientists tasked with securing their nations' nuclear stockpile.
They might create a simulation that tests if a physical part is going to properly perform a critical function for nuclear storage.
The physical part might last several decades, but the software often collapses much faster than that.
As our understanding of material science improves, they might want to reassess if the simulation still predicts the part performs its function properly given our improved understanding.
If the simulation experienced software collapse, this will need to be fixed, despite the software not changing.
Fixing the software may be difficult or impossible, especially if the original developer is retired.

\begin{enumerate}
\textbf{Reproducibility}
means "The measurement can be obtained with stated precision by a different team using the same measurement procedure, the same measuring system, under the same operating conditions, in the same or a different location on multiple trials. For computational experiments, this means that an independent group can obtain the same result using the author's own artifacts."
\textbf{Replicability}
means "The measurement can be obtained with stated precision by a different team, a different measuring system, in a different location on multiple trials. For computational experiments, this means that an independent group can obtain the same result using artifacts which they develop completely independently."
\end{enumerate}

\todo{Cite: https://www.acm.org/publications/policies/artifact-review-and-badging-current}

We define two "measurements" for the above definitions.

\begin{enumerate}
\item \textbf{Successful termination}
means whether the computational experiment runs to completion without error.
It may intuitively feel like a "measurement" should be continuous, but it there is no technical reason a measurement can't be a binary for the purposes of the definitions of repeatability, replicability, reproducibility.
If the experiment is a UNIX program, this usually means that it returns an exit code of 0.
\item \textbf{Resesarch output}
means the result of a computational experiment, as interpreted in the context of the research question it was designed to solve.
The context is important; bytewise different output might be close enough to imply the same result in the context of the research question.
\end{enumerate}

While reproducible research outputs are the end goal, that is difficult to automatically assess. reproducible successful termination is possible to automatically assess, and still a necessary condition for reproducible research outputs; if an experiment doesn't have reproducible successful termination, it can't have reproducible research outputs.

\section{Related Work}


Collberg et al. \todo{cite} gave an estimate of successfully terminating replicability only in computer science and only for certain journals. A many computational experiments are done by natural scientists.

Zhao et al. \todo{cite} gave an estimate of successfully terminating replicability using Taverna workflows. According to Zhao the situation is pretty dire (most things not replicable). However, Taverna has been replaced with newer tools, and it has not yet been published on whether these new tools actually help.

Trisovic et al. \todo{cite} give an estimate for R projects in Harvard Dataverse. There are technical reasons to believe that workflows will be more replicable than R projects. For example, if an experiment contains multiple R scripts, the Trisivoc study doesn't know which script to run first, but a workflow would have defined constraints on which script to run first.

Sridevi and Katiravan \todo{cite} look at a small-number of hand-picked workflows; I chose a large number of automatically executable workflows. They focus on producing an SVM that can predict failure, but their model is opaque. The correlations between observable features and successfully terminating replicability this study shows can be used to inform new hypotheses and future research.

\section{Methodology}

We are considering experiments which have been specifically published or uploaded to be in the repository.
Therefore, we assume that experiments did successfully terminate at the time they were published (although this does become a threat to validity).
For example, git commits are too frequent to be markers of working software, but git tags are less frequent and more likely to indicate working software.

When we run the experiment, we are a different team using the same measuring system (experiment), therefore we are testing its reproducibility.

\subsection{Research questions}

\begin{itemize}
\item \textbf{RQ1.} What are typical rates of software non-replicability?
\item \textbf{RQ2.} Does this correlate with time?
\item \textbf{RQ3.} Does this correlate with choice of workflow tool or language?
\item \textbf{RQ4.} Identify examples that are easy or hard to replicate. What makes these easy or hard to replicate?
\end{itemize}

\section{Results}

\todo{Link to results}

\todo{Table with results}

\section{Analysis}

\todo{Answer research questions}

\section{Discussion}


\subsection{Threats to validity}

\section{Conclusion}

\todo{Give domain scientist concrete takeaways}

\todo{Give SE researcher concrete takeaways}

\subsection{Future work}
