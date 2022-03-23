---
title: "Symmetry reduced Flag-hierarchies"
---
$$\require{color}$$
<!-- reveal-md slides.md -w --theme night -->
## Symmetry reduced Flag-hierarchies

-

### Daniel Brosch
<!-- #### Tilburg University -->
March 28, 2022

---

## Contents

- Semidefinite programming <!-- .element: class="fragment" data-fragment-index="1"-->
- Symmetry reduction basics <!-- .element: class="fragment" data-fragment-index="2" -->
- Representation theory of $S_n$ <!-- .element: class="fragment" data-fragment-index="3" -->
- Flag-Algebras <!-- .element: class="fragment" data-fragment-index="4" -->
- Lasserre style hierarchy <!-- .element: class="fragment" data-fragment-index="5" -->
- Razborov style hierarchy <!-- .element: class="fragment" data-fragment-index="6" -->
- Advanced ideas <!-- .element: class="fragment" data-fragment-index="7" -->

<div class="r-stack">

$$ \inf\\{\langle C,X\rangle : \langle A_i, X\rangle = b_i \forall i, X\succcurlyeq 0\\} $$ <!-- .element: class="fragment fade-in-then-out" data-fragment-index="1"-->

![](Pic_SymReduc.svg) <!-- .element: class="fragment fade-in-then-out" data-fragment-index="2"-->

</div>
---

## Semidefinite programming

<br />

<div class="r-stack">

$$ \inf_X\\{\langle C,X\rangle : \langle A_i, X\rangle = b_i \forall i, X\succcurlyeq 0\\} $$ <!-- .element: class="fragment fade-out" data-fragment-index="1" -->

$$ \inf_X\\{\langle C,X\rangle : \langle A_i, X\rangle = b_i \forall i, \fcolorbox{orange}{black}{$X\succcurlyeq 0$}\\} $$ <!-- .element: class="fragment fade-in-then-out" data-fragment-index="1" -->

</div> 

----

### The anatomy of an SDP

<div class="r-stack">

$$ \inf_X\\{\langle C,X\rangle : \langle A_i, X\rangle = b_i \forall i, X\succcurlyeq 0\\} $$ <!-- .element: class="fragment fade-out" data-fragment-index="1" -->

$$ \inf_X\\{\langle {\color{orange}C},X\rangle : \langle {\color{orange}A_i}, X\rangle = b_i \forall i, X\succcurlyeq 0\\} $$ <!-- .element: class="fragment fade-in-then-out" data-fragment-index="1" -->

$$ \inf_X\\{{\color{orange}\langle} C{\color{orange},}X{\color{orange}\rangle} : {\color{orange}\langle} A_i{\color{orange},}X{\color{orange}\rangle} = b_i \forall i, X\succcurlyeq 0\\} $$ <!-- .element: class="fragment fade-in-then-out" data-fragment-index="2" -->

$$ \inf_X\\{\langle C,X\rangle : \langle A_i, X\rangle = b_i \forall i, \fcolorbox{orange}{black}{$X\succcurlyeq 0$}\\} $$ <!-- .element: class="fragment fade-in-then-out" data-fragment-index="3" -->

$$ \inf_X\\{\langle C,X\rangle : \langle A_i, X\rangle = b_i \forall i, X\succcurlyeq 0\\} $$ <!-- .element: class="fragment fade-in-then-out" data-fragment-index="4" -->

</div> 

<br />

<div class="r-stack">

<div>$\color{orange} C, A_i\in\mathbb{S}^{n\times n}$ are symmetric data matrices </div> <!-- .element: class="fragment fade-in-then-out" data-fragment-index="1" -->

<div>$\color{orange} \langle\cdot,\cdot\rangle$ denotes the matrix inner product: $$\langle A,B\rangle = \sum_{i,j=1}^n A_{ij} B_{ij}$$ </div> <!-- .element: class="fragment fade-in-then-out" data-fragment-index="2" -->

$ \color{orange} X\succcurlyeq 0 $ says that $X$ is **positive semidefinite**: $$v^TXv\geq 0 \text{ for all vectors } v.$$  
<!-- .element: class="fragment fade-in-then-out" data-fragment-index="3" -->

SDPs are **linear optimization problems** over a **convex cone**. We can solve them in **polynomial time!**
<!-- .element: class="fragment fade-in-then-out" data-fragment-index="4" -->
</div> 

---

## SDP Symmetry reduction basics

<br />

![](Pic_SymReduc.svg) <!-- .element: class="r-stretch" -->

----

### What is a symmetry?


<br />

Let ${\color{orange}\sigma}$ be a **permutation** of $\\{1,\ldots, n\\}$. We let ${\color{orange}\sigma}$ act on the *indices of $X$ simultanously*:

$${\color{orange}\sigma}(X) = \left(X_{{\color{orange}\sigma}(i){\color{orange}\sigma}(j)}\right)_{i,j=1}^n.$$

<br />

<span class="fragment fade-in"><span class="r-frame">If $X$ is positive semidefinite, then $\sigma(X)$ is as well!</span></span>

----

### When does an SDP have a symmetry?

 
<div class="r-stack">

An SDP has symmetry $\sigma$, if $\sigma$ sends feasible solutions to feasible solutions with the same objective value. <!-- .element: class="fragment fade-out" data-fragment-index="1" -->

<span class="fragment fade-in" data-fragment-index="1">


This holds if for each constraint $\langle A_i,X\rangle=b_i$ there is a $j$ such that
 $$\sigma(A_i)=A_j, \quad b_i=b_j$$
and the objective is symmetric:
$$\sigma(C)=C.$$

</span></div>


----


### How do we exploit symmetries?


The set of all symmetries forms a **group $G$** of permutations. As the feasible set of an SDP is **convex**, we can **average** feasible solutions:

$$\mathcal{R}(X) = \frac{1}{|G|} \sum_{\sigma\in G}\sigma(X)$$


<span class="fragment fade-in" style="color:orange">

$\mathcal{R}(X)$ is again feasible, with the same objective value as $X$!

</span>

----

### Symmetric optimal solutions

<div class="r-stack">

<span class="fragment fade-out" data-fragment-index="1">
If $X^*$ is an optimal solution, then so is $\mathcal{R}(X^*)$. This solution is <span style="color:orange">invariant under actions of $G$</span>:
$$\sigma(\mathcal{R}(X^*)) = \mathcal{R}(X^*). $$
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

In the case of $G=D_{10}=C_5\times Z_2$ we can restrict $X$ to have the **pattern**

$$\begin{pmatrix}
{\color{red}A} & {\color{blue}B} & {\color{green}C} & {\color{green}C} & {\color{blue}B}\\\\
{\color{blue}B} & {\color{red}A} & {\color{blue}B} & {\color{green}C} & {\color{green}C}\\\\
{\color{green}C} & {\color{blue}B} & {\color{red}A} & {\color{blue}B} & {\color{green}C}\\\\
{\color{green}C} & {\color{green}C} & {\color{blue}B} & {\color{red}A} & {\color{blue}B} \\\\
{\color{blue}B} & {\color{green}C} & {\color{green}C} & {\color{blue}B} & {\color{red}A}\\\\
\end{pmatrix}$$ 
</span>
</div>

----

### Block-diagonalization
<div class="r-stack">

<span class="fragment fade-out" data-fragment-index="1">

$$\begin{pmatrix}
{\color{red}A} & {\color{blue}B} & {\color{green}C} & {\color{green}C} & {\color{blue}B}\\\\
{\color{blue}B} & {\color{red}A} & {\color{blue}B} & {\color{green}C} & {\color{green}C}\\\\
{\color{green}C} & {\color{blue}B} & {\color{red}A} & {\color{blue}B} & {\color{green}C}\\\\
{\color{green}C} & {\color{green}C} & {\color{blue}B} & {\color{red}A} & {\color{blue}B} \\\\
{\color{blue}B} & {\color{green}C} & {\color{green}C} & {\color{blue}B} & {\color{red}A}\\\\
\end{pmatrix}
$$

is positive semidefinite if and only if

* ${\color{red}A} + {\color{blue}B} + {\color{green}C} \geq 0$
* ${\color{red}A} +\frac{\sqrt{5}-1}{4}{\color{blue}B} - \frac{\sqrt{5}+1}{4}{\color{green}C} \geq 0$ 
* ${\color{red}A} -\frac{\sqrt{5}+1}{4}{\color{blue}B}+\frac{\sqrt{5}-1}{4}{\color{green}C} \geq 0$

</span>
<span class="fragment fade-in" data-fragment-index="1">
In general we may still get multiple bigger blocks

![](Pic_SymReduc.svg)

but <span style="color:orange">the sum of the block sizes is often significantly lower than $n$!</span>


</span>

Note: This linearizes the problem.

---
