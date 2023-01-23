# Work plan

- [x] 2023-01-16 Rerun failed experiments
- [ ] 2023-01-23 Get >30% pass on Nextflow, >10% on Snakemake, get at least 10 datapoints for each year from 2015 -- 2022.
- [ ] 2023-01-30 Finish draft (based on SC'S Delta Proposal and ICSE NIER)
- [ ] 2023-02-06 Deadline to submit

# Draft outline

- Introduction
  - Define reproducible, replicable, repeatable, software collapse
  - Motivate care for software collapse
  - Explain hole in prior research
- Methodology
  - Research questions:
    - What are typical rates of software non-replicability?
    - Does this correlate with time?
    - Does this correlate with choice of workflow tool or language?
    - Identify examples that are easy or hard to replicate. What makes these easy or hard to replicate?
  - Survey design
- Results
  - Link to results
  - Table with results
- Analysis
  - Answer research questions
- Discussion
  - Threats to validity
- Conclusion
  - Give domain scientist concrete takeaways
  - Give SE researcher concrete takeaways
- Future work

# Mary Shaw's guide to writing good SE papers

Mary Shaw wrote about [common and expected features of SE research papers][1], including the following:

[1]: https://www.cs.cmu.edu/~Compose/shaw-icse03.pdf

- What, precisely, was your contribution?
  - I will show the prevalence of un-replicable software in practice, and explain how that comes from either staleness or features of the software itself.
  - What question did you answer?
    - How many scientific experiments have successfully terminating replication?
  - Why should the reader care?
    - Science requires reproducibility to be self-correcting, successfully terminating replication is a necessary condition for reproducibility, it isn't always there in practice, and this study shows the prevalence of it, so we know the magnitude of the problem.
  - What larger question does this address?
    - Is computational replication a big problem in science?
- What is your new result?
  - If the correlation is positive with time, then new tools, policies, and incentives are helping to improve successfully-terminating replicability.
  - If my experiment shows that successfully-terminating replication (by extension reproducibility) is still difficult in practice, then computational replication is a big problem that hasn't been fixed despite the introduction of new tools, incentives, and policies. This is still an open research problem. On the other hand, if it shows successfully-terminating replication is common, then it shows that research should be focused on the gap between successfully-terminating replication and reproducibility.
 - In either case, we will have examples of what to do and what not to do, which guides readers in creating more replicable software.
 - What new knowledge have you contributed that the reader can use elsewhere?
  - What previous work (yours or someone else's) do you build on? What do you provide a superior alternative to?
    - Zhao et al. wrote software to do a similar experiment. Zhao's software is not open-source. Trisovic et al. have a similar open-source experiment. I develop an extended version of their system. Compared to Zhao and Trisovic, our system looks through more repositories, executes more workflow-types, measures more properties of the code, and computes correlations.
  - How is your result different from and better than this prior work?
    - Collberg et al. gave an estimate of successfully terminating replicability only in computer science and only for certain journals. A many computational experiments are done by natural scientists.
    - Zhao et al. gave an estimate of successfully terminating replicability using Taverna workflows. According to Zhao the situation is pretty dire (most things not replicable). However, Taverna has been replaced with newer tools, and it has not yet been published on whether these new tools actually help.
    - Trisovic et al. give an estimate for R projects in Harvard Dataverse. There are technical reasons to believe that workflows will be more replicable than R projects. For example, if an experiment contains multiple R scripts, the Trisivoc study doesn't know which script to run first, but a workflow would have defined constraints on which script to run first.
    - Sridevi and Katiravan look at a small-number of hand-picked workflows; I chose a large number of automatically executable workflows. They focus on producing an SVM that can predict failure, but their model is opaque. The correlations between observable features and successfully terminating replicability this study shows can be used to inform new hypotheses and future research.
  - What, precisely and in detail, is your new result?
    - To be determined.
- Why should the reader believe your result?
  - I test on a lot of different experiments from different repositories. A lot of journals and grant-funding agencies have a requirement that experiments be put into public repositories, so we expect this to be quite a large net.
  - What standard should be used to evaluate your claim?
    - Run our software on new experiments or new repositories. Even running the exact same experiment a year from now would catch new experiments deposited in that last year. Are these experiments replicable at a similar rate?
  - What concrete evidence shows that your result satisfies your claim?
    - TBD
