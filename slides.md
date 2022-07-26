---
title: "Symmetry reduced Flag-hierarchies"
---
$$\require{color}$$
<!-- reveal-md slides.md -w --theme night -->
<!-- reveal-md slides.md --theme night --static _site -->
<!-- Then copy videos! -->
<!-- and remove _asset paths -->
### Möbius-transformation based symmetry reduction
With application to flag sums-of-squares

<br/>

#### Daniel Brosch
#### Tilburg University $\rightarrow$ Klagenfurt University

<br/>
July 26, 2022

---


## Flag-Algebras

![](Pic_FlagExample.svg)


----

### Flag-Algebras

<span class="r-stack">
<span class="fragment fade-out" data-fragment-index="1">

Flag-Algebras were first introduced by **Alexander Razborov** in 2007, and remain one of the most powerful tools in <span style="color:orange">extremal combinatorics</span>. 

</span>
<span class="fragment fade-in" data-fragment-index="1">

They have been used to investigate to <span style="color:orange">dense limits</span> of

- graphs, <!-- .element: class="fragment" data-fragment-index="1"-->
- hypergraphs, <!-- .element: class="fragment" data-fragment-index="2"-->
- directed graphs, <!-- .element: class="fragment" data-fragment-index="3"-->
- permutations, <!-- .element: class="fragment" data-fragment-index="4"-->
- point order types, <!-- .element: class="fragment" data-fragment-index="5"-->
- and much more! <!-- .element: class="fragment" data-fragment-index="6"-->

<span> In this talk, we will focus on the case of <span style="color:orange">graphs</span>.</span> <!-- .element: class="fragment" data-fragment-index="7"-->

</span>
</span>


Note: Razborov unifies and generalizes ideas of many authors.


----

### How many edges can there be in a triangle free graph?

<video class="fv-video" src="./videos/TriangleFree.mp4" fv-playback-info="./videos/TriangleFree.json">
</video>

----

### Triangle free graphs

<div class="r-stack">
<div class="fragment fade-out" data-fragment-index="2">

To formally define the optimization problem, we let

$${\color{orange}\mathcal{G}} = ({\color{orange}G_i})_{i\geq 1}$$

be a <span style="color:orange">sequence of graphs</span>, where each graph $\color{orange}G_i$ has $i$ vertices.

<div class="fragment fade-in" data-fragment-index="1">
<div class="r-frame">
The <span style="color:orange">density</span> of a graph $\color{green}H$ in $\color{orange}\mathcal{G}$ is
$$p({\color{orange}\mathcal{G}}, {\color{green}H}) := \lim_{i\to\infty} \mathbb{P}[{\color{red}\sigma_i}({\color{green}H}) \text{ is a subgraph of }{\color{orange}G_i}],$$
where ${\color{red}\sigma_i}$ is a random permutation in $S_i$.
</div>
</div>
</div>
<div class="fragment fade-in" data-fragment-index="2">

Maximize the <span style="color:orange">edge density</span> in a <span style="color:green">triangle free</span> sequence $\mathcal{G}$ of graphs of increasing size:

![](Pic_EqTriangleFree.svg)

We saw that

![](Pic_EqTriangleFreeLowerBound.svg)

but how do we find an <span style="color:orange">upper bound</span>?

</div>
</div>

Note: Non-induced subgraphs count

----

### Multiplying subgraph densities



<div class="r-stack">
<div class="fragment fade-out" data-fragment-index="2">
If we multiply two subgraph densities, we <span style="color:orange">glue together</span> the graphs:

![](Pic_DensityProduct.svg)

<div class="fragment fade-in" data-fragment-index="1">
Because the probability that the two graphs are sent to <span style="color:orange">disjoint</span> sets of vertices <span style="color:orange">converges to $1$ in the limit</span>. 
</div>
</div>
<div class="fragment fade-in-then-out" data-fragment-index="2">
These relationships are <span style="color:orange">independent of $\mathcal{G}$</span>, motivating the notation

![](Pic_DensityProductNoP.svg)

where a graph $H$ now stands for the function
$$H(\mathcal{G}) =  p(\mathcal{G},H).$$
</div>
<div class="fragment fade-in" data-fragment-index="3">

We can now restrict the randomly chosen permutations $\sigma_i$ to fix (<span style="color:orange">flag</span>) some vertices, and extend the <span style="color:orange">gluing</span> operation to <span style="color:orange">partially labeled graphs (Flags)</span>:

![](Pic_FlagExample.svg)

</div>
</div>

----

### Flag Sums-of-Squares

<div class="r-stack">
<div class="fragment fade-out" data-fragment-index="2">

As Flags send graph sequences to *real numbers*, <span style="color:orange">squaring a linear combination of Flags</span> results in a function that sends graph sequences to a <span style="color:orange">nonnegative number</span>:

![](Pic_FlagSOS1.svg)

<span class="fragment fade-in" data-fragment-index="1">A linear combination of Flags is called a <span style="color:orange">Quantum-Flag</span>.</span>
</div>
<div class="fragment fade-in-then-out" data-fragment-index="2">
We can <span style="color:orange">average</span> Flags over all choices of labels, <span style="color:orange">unlabeling</span> them:

![](Pic_FlagSOS2.svg)

Note: Averaging preserves nonnegativity.

</div>

<div class="fragment fade-in" data-fragment-index="3">

We can now find an <span style="color:orange">upper bound</span> for the edge density in triangle free graphs:

![](Pic_FlagSOS3.svg)

<div class="fragment fade-in" data-fragment-index="4">

As for <span style="color:orange">polynomial optimization</span>, we can model Flag-SOS using <span style="color:orange">semidefinite programming</span>.

</div>
</div>
</div>

---

### Flags as (limits of) polynomials

<div class="r-stack">
<div class="fragment fade-out" data-fragment-index="2">

Recently, **Raymond**, **Saunderson**, **Singh** and **Thomas** have proven a fascinating connection of <span style="color:orange">Flag-SOS</span> and <span style="color:orange">polynomial SOS</span>: 

<br/>

- Flags can be seen as limits of sequences of polynomials.
- <span style="color:orange">Partially</span> exploiting the polynomials' symmetries and taking the limit leads to Flag-SOS.

<span style="color:orange">We exploit their symmetries fully!</span><!-- .element: class="fragment" data-fragment-index="1"-->
</div>
<div class="fragment fade-in-then-out" data-fragment-index="2">

Maximizing the <span style="color:orange">edge density</span> in a <span style="color:green">triangle</span>-free graph can be reformulated as:

\begin{align}
    \lim_{n\to\infty}\max \enspace&{\color{orange}\frac{1}{\binom n 2}\sum_{1\leq i<j\leq n} x_{ij}}\\\\
    \text{s.t.}\enspace & {\color{green}\frac{1}{\binom{n}{3}}\sum_{1\leq i<j<k\leq n} x_{ij}x_{ik}x_{jk}} = 0,\\\\
    & x_{ij}\in\\{0,1\\} \quad \text{for all } i < j.
\end{align}

</div>
<div class="fragment fade-in" data-fragment-index="3">

We introduce <span style="color:orange">binary</span> variables corresponding to <span style="color:orange">edges</span>:

$$ x_{ij} \in \\{0,1\\} \quad \text{for } i < j. $$

<div class="fragment" data-fragment-index="4">

Subgraph densities are polynomials <span style="color:orange">invariant</span> under $\color{orange}{S_n}$ acting simultanously on the indices:

$${\color{orange}\sigma}(x_{ij}) = x_{{\color{orange}\sigma}(i){\color{orange}\sigma}(j)}.$$

<div class="fragment" data-fragment-index="5" style="color:orange">
We can exploit this symmetry!
</div>

</div>

</div>
</div>

Note: Monomials = fully labeled graphs. Action corresponds to permuting labels.

---

### Main reduction idea:

Formulate the problem as a <span style="color:orange">sequence</span> of highly <span style="color:orange">symmetric</span> polynomial optimization problems

<br/>

<div class="fragment">

<span style="color:orange">Exploit</span> the symmetries for <span style="color:orange">each finite $n$</span>

</div>

<br/>

<div class="fragment">

The resulting hierarchies have block-sizes <span style="color:orange">independent of $n$</span>, we can <span style="color:orange">take the limit!</span>

</div>


---

## Main contributions

<div class="r-stack">
<div class="fragment fade-out" data-fragment-index="1">

We fully <span style="color:orange">exploit the symmetries</span> of two hierarchies:

- <span style="color:orange">Lasserre</span> hierarchy for Flags with <span style="color:orange">few edges</span>       

- <span style="color:orange">Razborov</span> hierarchy for Flags with <span style="color:orange">few vertices</span>     

<br/>

This talk focuses on the <span style="color:orange">Razborov hierarchy.</span>

</div>

<div class="fragment fade-in" data-fragment-index="1">

We lay the groundwork for a few novel ideas:


<span class="fragment" data-fragment-index="2">Extension of Flag-Algebras to <span style="color:orange">degenerate extremal combinatorics</span>.</span>

<div class="fragment" data-fragment-index="3">

A <span style="color:orange">harmonic basis</span> and <span style="color:orange">Fourier decomposition</span> of Flags.

</div>

<div class="fragment" data-fragment-index="4">

A generalization of Razborov's <span style="color:orange">partial derivatives</span> of Flags.

</div>
</div>


</div>


---

## SDP Symmetry reduction basics

<br />

![](Pic_SymReduc.svg) <!-- .element: class="r-stretch" -->

----

### Symmetric sums of squares


$S_n$ acts here on the basis ${\color{red}[x]}$ of monomials.

This action <span style="color:orange">permutes the rows and columns</span> of the <span style="color:orange">positive semidefinite matrix $X$</span> in the <span style="color:orange">SOS-term</span>

\begin{align}
{\color{orange}\sigma}({\color{red}[x]}^TX{\color{red}[x]}) &= {\color{orange}\sigma}({\color{red}[x]})^TX{\color{orange}\sigma}({\color{red}[x]})\\\\
&= {\color{red}[x]}^T\left(X_{{\color{orange}\sigma}(m_1),{\color{orange}\sigma}(m_2)}\right)_{m_1,m_2\in {\color{red}[x]}}{\color{red}[x]}\\\\
&= {\color{red}[x]}^T{\color{orange}\sigma}(X){\color{red}[x]}
\end{align}



<span class="fragment fade-in" style="color:orange">If $X$ is positive semidefinite, then ${\color{orange}\sigma}(X)$ is as well!</span>

----


### How do we exploit symmetries?

As the feasible set of an SDP is **convex**, we can **average** feasible solutions:

$$\mathcal{R}(X) = \frac{1}{|{\color{orange}G}|} \sum_{{\color{orange}\sigma}\in {\color{orange}G}}{\color{orange}\sigma}(X)$$


<span class="fragment fade-in" style="color:orange">

$\mathcal{R}(X)$ is again feasible, with the same objective value as $X$!

</span>

----

### Symmetric optimal solutions

<div class="r-stack">

<span class="fragment fade-out" data-fragment-index="1">
If $X^*$ is an optimal solution, then so is $\mathcal{R}(X^*)$. This solution is <span style="color:orange">invariant under actions of ${\color{orange}G}$</span>:
$${\color{orange}\sigma}(\mathcal{R}(X^*)) = \mathcal{R}(X^*). $$
</span>
<span class="fragment fade-in-then-out" data-fragment-index="1">

We can restrict the SDP to optimize only over <span style="color:orange">invariant</span> matrices:
\begin{align}
\inf\enspace&\langle C,X\rangle \\\\
\text{s.t.}\enspace& \langle A_i, X\rangle = b_i\quad \text{for all } i,\\\\
& X\succcurlyeq 0,\\\\
& {\color{orange}\mathcal{R}(X)=X}.\\\\
\end{align}

</span>
<span class="fragment fade-in-then-out" data-fragment-index="2">

In the case of ${\color{orange}G}=D_{10}=C_5\times Z_2$ we can restrict $X$ to have the **pattern**

$$\begin{pmatrix}
{\color{red}A} & {\color{orange}B} & {\color{green}C} & {\color{green}C} & {\color{orange}B}\\\\
{\color{orange}B} & {\color{red}A} & {\color{orange}B} & {\color{green}C} & {\color{green}C}\\\\
{\color{green}C} & {\color{orange}B} & {\color{red}A} & {\color{orange}B} & {\color{green}C}\\\\
{\color{green}C} & {\color{green}C} & {\color{orange}B} & {\color{red}A} & {\color{orange}B} \\\\
{\color{orange}B} & {\color{green}C} & {\color{green}C} & {\color{orange}B} & {\color{red}A}\\\\
\end{pmatrix}$$ 
</span>
</div>

----

### Block-diagonalization
<div class="r-stack">

<span class="fragment fade-out" data-fragment-index="1">

$$\tiny\begin{pmatrix}
{\color{red}A} & {\color{orange}B} & {\color{green}C} & {\color{green}C} & {\color{orange}B}\\\\
{\color{orange}B} & {\color{red}A} & {\color{orange}B} & {\color{green}C} & {\color{green}C}\\\\
{\color{green}C} & {\color{orange}B} & {\color{red}A} & {\color{orange}B} & {\color{green}C}\\\\
{\color{green}C} & {\color{green}C} & {\color{orange}B} & {\color{red}A} & {\color{orange}B} \\\\
{\color{orange}B} & {\color{green}C} & {\color{green}C} & {\color{orange}B} & {\color{red}A}\\\\
\end{pmatrix}
$$

is positive semidefinite if and only if

* ${\color{red}A} + {\color{orange}B} + {\color{green}C} \geq 0$,
* ${\color{red}A} +\frac{\sqrt{5}-1}{4}{\color{orange}B} - \frac{\sqrt{5}+1}{4}{\color{green}C} \geq 0$,
* ${\color{red}A} -\frac{\sqrt{5}+1}{4}{\color{orange}B}+\frac{\sqrt{5}-1}{4}{\color{green}C} \geq 0$.

</span>
<span class="fragment fade-in" data-fragment-index="1">
In general we may still get multiple bigger blocks

![](Pic_SymReduc.svg)

but <span style="color:orange">the sum of the block sizes is often significantly lower than $n$!</span>

</span>
</div>

Note: This linearizes the problem.

---

## Lasserre style hierarchy
#### Prioritizing Flags with <span style="color:orange">few edges</span>


<!-- 
<img class="r-stretch" src="Pic_SpechtFlags.svg"> -->

----

### The Lasserre hierarchy

<div class="r-stack">
<div class="fragment fade-out" data-fragment-index="2">

The $\color{orange}d$'th level of the <span style="color:orange">Lasserre hierarchy</span> limits the <span style="color:orange">degree</span> of appearing monomials to at most $2{\color{orange}d}$.

<br/>

<div class="fragment" data-fragment-index="1">
We optimize over sums of squares of the form

$${\color{red}[x]}^T X  {\color{red}[x]},$$

where $X\succcurlyeq 0$ and ${\color{red}[x]}$ is a basis of 
$$ \mathbb{R}[x]_{\leq {\color{orange}d}}.$$


</div>

</div>
<div class="fragment fade-in" data-fragment-index="2">

As monomials correspond to <span style="color:orange">fully labeled graphs</span>, we here have

$${\color{red}[x]} = \\{H : H \text{ graph with at most $\color{orange}d$ edges}\\}.$$

</div>
</div>


----

### Reducing the Lasserre hierarchy

<div class="r-stack">
<div class="fragment fade-out" data-fragment-index="1">

New tools for the <span style="color:orange">representation theory of $S_n$:</span> We can decompose <span style="color:orange">quotients of permutation modules</span>
$$ M^\lambda / G,$$
where $G$ acts on the rows of $\lambda$ into <span style="color:orange">irreducible submodules</span>.

</div>
<div class="fragment fade-in" data-fragment-index="1">

This results in a <span style="color:orange">symmetry adapted basis</span> for flag algebras, which we call <span style="color:orange">Specht-flags</span>:
<img class="r-stretch" src="Pic_SpechtFlags.svg">


</div>
</div>


<span style="color:orange">But this is not the focus of this talk.</span>
<!-- .element: class="fragment" data-fragment-index="2"-->


---

## Razborov style hierarchy
#### Prioritizing Flags with <span style="color:orange">few vertices</span>

----

### Möbius-transformations

<div class="r-stack">
<div class="fragment fade-out" data-fragment-index="1">

Well-known fact: <span style="color:orange">The $n$'th level of the Lasserre hierarchy is sharp.</span> 

<br/>

<span style="color:orange">Proof idea:</span> Applying a <span style="color:orange">Möbius-transformation</span> to the rows and columns of the SDP <span style="color:orange">diagonalizes</span> the hierarchy.

</div>
<div class="fragment fade-in-then-out" data-fragment-index="1">

<span style="color:orange">Example:</span> Optimize over two binary variables $x_1,x_2\in\\{0,1\\}.$

<br/>

The second level of the <span style="color:orange">Lasserre hierarchy</span> involves a matrix $\color{orange}X$ of the form
$$\small\begin{pmatrix}1 & x_1 & x_2 & x_1x_2\\\\
x_1 & x_1 & x_1x_2 & x_1x_2\\\\
x_2 & x_1x_2 & x_2 & x_1x_2\\\\
x_1x_2 & x_1x_2 & x_1x_2 & x_1x_2\end{pmatrix} $$

</div>
<div class="fragment fade-in-then-out" data-fragment-index="2">

The <span style="color:orange">Möbius-transformation</span> assigns the following

$$\begin{align}1 &\longrightarrow (1-x_1)(1-x_2)\\\\
x_1 &\longrightarrow x_1(1-x_2)\\\\
x_2 & \longrightarrow (1-x_1)x_2\\\\
x_1x_2 & \longrightarrow x_1x_2\end{align}$$

<span style="color:orange">We multiply monomials $m$ with $(1-x_i)$ for all $x_i$ not appearing in $m$.</span>

</div>
<div class="fragment fade-in" data-fragment-index="3">

As $\color{orange}x_i(1-x_i)=0$, applying the transformation to the rows and columns of $\color{orange}X$ diagonalizes the matrix:

$$\scriptsize\substack{\begin{pmatrix}1 & x_1 & x_2 & x_1x_2\\\\
x_1 & x_1 & x_1x_2 & x_1x_2\\\\
x_2 & x_1x_2 & x_2 & x_1x_2\\\\
x_1x_2 & x_1x_2 & x_1x_2 & x_1x_2\end{pmatrix} \\\\\downarrow \\\\\begin{pmatrix}(1-x_1)(1-x_2) & & &\\\\&x_1(1-x_2)&&\\\\&&(1-x_1)x_2&\\\\&&&x_1x_2\end{pmatrix}}$$


</div>
</div>

----

### Möbius-transformation based symmetry reduction

Normally, we can only apply the transformation to the <span style="color:orange">final level</span> of the Lasserre hierarchy.

<br/>

We <span style="color:orange">truncate</span> the Lasserre hierarchy in such a way, that we can <span style="color:orange">apply the transformation earlier</span> to sub-problems, partially diagonalizing it.

----

### Back to flag algebras

We are in the setting of 
- <span style="color:orange">variables</span> $x_{ij}\in\\{0,1\\}$ corresponding to <span style="color:orange">edges</span>,
- <span style="color:orange">monomials</span> $m$ corresponding to <span style="color:orange">graphs.</span>

----

### Prioritizing small graphs

<div class="r-stack">

<!-- STACK 1 -->
<div class="fragment fade-out" data-fragment-index="2">

**Razborov** prioritizes Flags with <span style="color:orange">few vertices</span>. Let $\color{green}T$ be the maximum number of vertices we want to appear. 

<div class="fragment" data-fragment-index="1">
<div class="r-frame">
We optimize over sums of squares
$$\sum p_i^2, $$
where <span style="color:orange">each square</span> $p_i^2$ does not contain a monomial with more than $\color{green}T$ vertices.
</div>
</div>

</div>
<!-- STACK 2 -->

<div class="fragment fade-in-then-out" data-fragment-index="2">
We optimize over

$${\color{red}[x]}^T X  {\color{red}[x]},$$

where ${\color{red}[x]}$ contains monomials with at most ${\color{green}T}$ vertices, where $X$ has a <span style="color:orange">rank one decomposition</span>
$$X = X_1 + \ldots + X_k,$$
where each ${\color{red}[x]}^T X_i  {\color{red}[x]}$ is a linear combination of graphs with at most $\color{green}T$ vertices.

</div>

<!-- STACK 3 -->
<div class="fragment fade-in" data-fragment-index="3">

The $X_i$ correspond exactly to the <span style="color:orange">maximal 
cliques</span> in the sparsity pattern given by
$$ (X_i)_{G,H} = 0 \quad\text{if $GH$ has more than $\color{green}T$ vertices}.$$

</div>

</div>


----

### The maximal cliques

For each ${\color{orange}K}\leq {\color{green}T}$ with ${\color{orange}K}\enspace\mathrm{mod}\enspace 2\equiv {\color{green}T}$, the maximal clique $\mathcal{B}_{\color{orange}K}$ contains the graphs of the form:


<img class="r-stretch" src="./CliqueGraphs.svg">
<!-- <img src="./CliqueGraphs.png"> -->


<div class="fragment">
<span style="color:orange">Products of graphs within the same $\mathcal{B}_{\color{orange}K}$ result in a graph with at most $\color{gree}T$ vertices!</span>
</div>

----

### Symmetry reduction

Symmetry reduction is trivial: <span style="color:orange">We only consider the maximal cliques up to symmetry!</span>

----

### Möbius transformation

Each clique $\mathcal{B}_{\color{orange}K}$ is closed under addition of edges within $[{\color{orange}K}]$.

<br/>

<div class="fragment">

<span style="color:orange">$\longrightarrow$ Möbius-transformation on the first $\color{orange}K$ vertices</span>. 

If $G\vert_{[{\color{orange}K}]} \neq H\vert_{[{\color{orange}K}]}$, then the product of the transformed graphs is zero.


</div>

<br/>

<span style="color:orange">$\longrightarrow$ One block for each graph. We only need graphs up to isomorphism!</span> <!-- .element: class="fragment"-->


----

### Breaking Schur's Lemma

<div class="r-stack">
<div class="fragment fade-out" data-fragment-index="2">

<div class="r-frame">

Let $\color{orange}M$, $\color{orange}N$ be two **irreducible** $G$-modules over a ring $R$. Let ${\color{limegreen}\varphi} : {\color{orange}M}\to {\color{orange}N}$ be a homomorphism.

- If $\color{orange}M$ and $\color{orange}N$ are not isomorphic, then ${\color{limegreen}\varphi} \equiv 0$. 
- If ${\color{orange}M}\simeq {\color{orange}N}$ and $R$ is an <span style="color:red">algebraically closed field</span>, then ${\color{limegreen}\varphi} = c\mathrm{I}$ for a $c\in R$. 

</div>

<br/>

<div class="fragment" data-fragment-index="1">
We optimize over $\{0,1\} = \mathbb{Z}_2$, which is <span style="color:orange">not algebraically closed!</span>
</div>

</div>
<div class="fragment fade-in" data-fragment-index="2">

<img class="r-stretch" src="Pic_BreakingSchurs.svg">

Both modules are <span style="color:orange">isomorphic</span> to the module $M^{(1,1)}$, but also <span style="color:orange">orthogonal</span> to each other, as $x_{12}(1-x_{12}) = 0$.
</div>

</div>

----

### Additional symmetries

We obtain <span style="color:orange">one block for each graph $\color{green}G$ with up to $\color{green}T$ vertices</span>.

<br/>

<div class="fragment" data-fragment-index="4">
The symmetries of each block are now given by
$$\mathrm{Aut}({\color{green}G}) \times S_{n-|V({\color{green}G})|} $$
<span style="color:red">The symmetry groups are complicated!</span>

</div>

<br/>

<div class="fragment" data-fragment-index="5">
We can still block-diagonalize the algebra numerically.
</div>

</div>

----

### Connection to Razborov's hierarchy

We obtain blocks for each Graph ${\color{green}G}$ with symmetry
$$\mathrm{Aut}({\color{green}G}) \times S_{n-|V({\color{green}G})|}. $$

We obtain the <span style="color:orange">Flag Algebra $\mathcal{A}^{\color{green}G}$ of <span style="color:orange">type</span> ${\color{green}G}$ </span>by restricting to the elements invariant under 
$$S_{n-|V({\color{green}G})|}.$$
----

### Comparing the hierarchies

In the setting of (undirected) graphs we have 
  \begin{equation}
    \mathrm{Las}_{2{\color{orange}d}} \geq \mathrm{Raz} _{4\color{orange}d}\geq  \mathrm{Vert} _{4{\color{orange}d}}
  \end{equation}
  and
  \begin{equation}
    \mathrm{Raz} _{\color{green}T} \geq \mathrm{Vert} _{\color{green}T} \geq \mathrm{Las} _{2\binom{{\color{green}T}}{2}},
  \end{equation}
where <span style="color:orange">lower means better</span>.
---

### Graph-profiles

<div class="r-stack">
<div class="fragment fade-out" data-fragment-index="1">

Let $\color{orange}G$ and $\color{green}H$ be two (Quantum-)Graphs.

The <span style="color:orange">Graph-profile</span> of $\color{orange}G$ and $\color{green}H$ is the set of possible values

$$\left\lbrace (p(\mathcal{G}, {\color{orange}G} ), p(\mathcal{G}, {\color{green}H} )) : \mathcal{G} \text{ sequence of graphs}\right\rbrace.$$

</div>
<div class="fragment fade-in-then-out" data-fragment-index="1">

<span style="color:orange">Razborov</span> calculates the <span style="color:orange">triangle</span>-<span style="color:green">edge</span> graph profile:

<img src="./TriangleProfile.png" width="675" height="450">

<!-- <img class="plain" src="TriangleProfile.png"> -->

<!-- ![](TriangleProfile.png) -->


</div>
<div class="fragment fade-in-then-out" data-fragment-index="2">

We can find an <span style="color:orange">outer approximation</span> of graph profiles by solving

$$\max \int_0^1 f \text{ s.t. } {\color{orange}G} - f({\color{green}H}) \geq 0,$$

for a lower bound, where $f$ is a <span style="color:orange">univariate</span> polynomial. We solve a similar problem for an upper bound.


</div>

<div class="fragment fade-in-then-out" data-fragment-index="3">

One function is not enough:
<img src="./TriangleProfileApprox.png" width="675" height="450">

</div>
<div class="fragment fade-in" data-fragment-index="4">


Cutting $[0,1]$ into many intervals works well:

<img src="./TriangleProfileSteps.png" width="675" height="450">


</div>
</div>

Note: Very few known; edge + Kn, some approximations of slices of profile of small graphs.

----


<img class="r-stretch" src="./GraphProfiles.png">

----

## Harmonic Flags

We found a basis of the Flag-Algebra of elements we call <span style="color:orange">harmonic Flags</span>. These come from the <span style="color:orange">characters of the binary hypercube</span>, and are a basis of <span style="color:orange">limits of orthogonal polynomials</span>.

----


<img class="r-stretch" src="./GraphProfilesHarmonic.png">


---

## Software

A Julia package implementing the fully reduced hierarchies (and much more!) for <span style="color:orange">arbitrary Flags</span> will be available very soon.

--- 

## Paper

Should be online soon-ish. It will be first available as part of <span style="color:orange">my thesis draft</span>.