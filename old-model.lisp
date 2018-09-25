; it is not possible to run this model with the modified python code,
; but it can still be run by setting the letter in line 79 and
; loading it into ACT-R manually

(clear-all)

(define-model project

(sgp :v nil :esc t :egs 3 :show-focus t :ul t :ult t :needs-mouse t)

(chunk-type outline letter s0 d0 s1 d1 s2 d2 s3 d3 s4 d4 s5 d5 s6 d6)
(chunk-type goal letter state coor)
(chunk-type stroke p1 p2)
(chunk-type sequence identity next)

(install-device '("motor" "cursor" "mouse"))
(start-hand-at-mouse)

;; add the whole chunk to imaginal

(add-dm
  (one ISA sequence identity s0 next d0)
  (two ISA sequence identity d0 next s1)
  (three ISA sequence identity s1 next d1)
  (four ISA sequence identity d1 next s2)
  (five ISA sequence identity s2 next d2)
  (six ISA sequence identity d2 next s3)
  (seven ISA sequence identity s3 next d3)
  (eight ISA sequence identity d3 next s4)
  (nine ISA sequence identity s4 next d4)
  (ten ISA sequence identity d4 next s5)
  (eleven ISA sequence identity s5 next d5)
  (twelve ISA sequence identity d5 next s6)
  (thirteen ISA sequence identity s6 next d6)

  (A ISA outline s0 c01 d0 c10 s1 c10 d1 c20 s2 c01 d2 c12 s3 c12 d3 c22
                 s4 c10 d4 c12)
  (B ISA outline s0 c00 d0 c02 s1 c00 d1 c02 s2 c02 d2 c12 s3 c12 d3 c10
                 s4 c10 d4 c12 s5 c12 d5 c22 s6 c22 d6 c20)
  (C ISA outline s0 c02 d0 c00 s1 c00 d1 c20 s2 c20 d2 c22)
  (D ISA outline s0 c00 d0 c02 s1 c00 d1 c01 s2 c01 d2 c12 s3 c12 d3 c21
                 s4 c21 d4 c20)
  (E ISA outline s0 c00 d0 c20 s1 c00 d1 c02 s2 c10 d2 c12 s3 c20 d3 c22)
  (F ISA outline s0 c00 d0 c20 s1 c00 d1 c02 s2 c10 d2 c12)
  (G ISA outline s0 c02 d0 c00 s1 c00 d1 c20 s2 c20 d2 c22 s3 c22 d3 c12
                 s4 c12 d4 c11)
  (H ISA outline s0 c00 d0 c20 s1 c10 d1 c12 s2 c02 d3 c22)
  (I ISA outline s0 c00 d0 c02 s1 c01 d1 c21 s2 c20 d2 c22)
  (J ISA outline s0 c00 d0 c02 s1 c01 d1 c21 s2 c21 d2 c20)
  (K ISA outline s0 c00 d0 c20 s1 c02 d2 c10 s3 c10 d3 c22)
  (L ISA outline s0 c00 d0 c20 s1 c20 d1 c22)
  (M ISA outline s0 c00 d0 c20 s1 c00 d1 c21 s2 c21 d2 c02 s3 c02 d3 c22)
  (N ISA outline s0 c00 d0 c20 s1 c00 d1 c22 s2 c02 d2 c22)
  (O ISA outline s0 c00 d0 c20 s1 c02 d1 c22 s2 c22 d2 c02 s3 c02 d3 c00)
  (P ISA outline s0 c00 d0 c20 s1 c00 d1 c02 s2 c02 d2 c12 s3 c12 d3 c10)
  (Q ISA outline s0 c00 d0 c20 s1 c20 d1 c21 s2 c21 d2 c12 s3 c12 d3 c02
                 s4 c02 d4 c00 s5 c11 d5 c22)
  (R ISA outline s0 c00 d0 c20 s1 c00 d1 c02 s2 c02 d2 c12 s3 c12 d3 c10
                 s4 c10 d4 c22)
  (S ISA outline s0 c02 d0 c00 s1 c00 d1 c10 s2 c10 d2 c12 s3 c12 d3 c22
                 s4 c22 d4 c20)
  (T ISA outline s0 c00 d0 c02 s1 c01 d1 c21)
  (U ISA outline s0 c00 d0 c20 s1 c20 d1 c22 s2 c22 d2 c02)
  (V ISA outline s0 c00 d0 c10 s1 c10 d1 c21 s2 c21 d2 c12 s3 c12 d3 c02)
  (W ISA outline s0 c00 d0 c20 s1 c20 d1 c11 s2 c11 d2 c22 s3 c22 d3 c02)
  (X ISA outline s0 c00 d0 c22 s1 c20 d1 c02)
  (Y ISA outline s0 c00 d0 c11 s1 c02 d1 c11 s2 c11 d2 c21)
  (Z ISA outline s0 c00 d0 c02 s1 c02 d1 c20 s2 c20 d2 c22)

  (c00 ISA visual-location screen-x 20 screen-y 20)
  (c01 ISA visual-location screen-x 40 screen-y 20)
  (c02 ISA visual-location screen-x 60 screen-y 20)
  (c10 ISA visual-location screen-x 20 screen-y 50)
  (c11 ISA visual-location screen-x 40 screen-y 50)
  (c12 ISA visual-location screen-x 60 screen-y 50)
  (c20 ISA visual-location screen-x 20 screen-y 80)
  (c21 ISA visual-location screen-x 40 screen-y 80)
  (c22 ISA visual-location screen-x 60 screen-y 80)

  (goal isa goal state start letter G)
  (start) (retrieval) (move) (click) (increment) (outline-failure)
  (increment-failure) (success)
  (s0) (d0) (s1) (d1) (s2) (d2) (s3) (d3) (s4) (d4) (s5) (d5) (s6) (d6)
  )

;;retrieve letter
(p start-retrieve
    =goal>
      ISA         goal
      state       start
      letter      =letter
  ==>
    =goal>
      ISA         goal
      state       retrieval
    +retrieval>
      ISA         outline
      letter      =letter
)

(p fail-retrieve
    =goal>
      ISA         goal
      state       retrieval
    ?retrieval>
      buffer      failure
  ==>
    =goal>
      ISA         goal
      state       outline-failure
)

;; retrieve stroke

;; retrieve -> encode into imaginal -> retrieve s0 -> retrieve starting point ->
;; prepare-mouse -> click to start -> retrieve endpoint -> move-mouse-to-location
;;-> click to end -> increment slot name -> repeat...

(p encode-letter
    =goal>
      ISA         goal
      state       retrieval
      letter      =letter
    =retrieval>
      ISA         outline
      letter      =letter
    ?imaginal>
      state       free
      buffer      empty
  ==>
    =goal>
      ISA         goal
      state       move
      coor        s0
      letter      =letter
    +imaginal>    =letter
    +retrieval>
      ISA         sequence
      identity    s0
)



(p start-coordinate
    =goal>
      ISA         goal
      state       move
      coor        =coor
    =imaginal>
      =coor       =loc
    ?manual>
      state       free
  ==>
    !output!      (Move =loc)
    =goal>
      ISA         goal
      state       click
    +manual>
      cmd         move-cursor
      loc         =loc
    =imaginal>
)

(p click-mouse
    =goal>
      ISA         goal
      state       click
      coor        =coor
    =retrieval>
      ISA         sequence
      identity    =coor
      next        =next
    ?manual>
      state       free
  ==>
    !output!      (Click =coor)
    =goal>
      ISA         goal
      state       increment
      coor        =coor
    +manual>
      cmd         click-mouse
    +retrieval>
      ISA         sequence
      identity    =coor
)

(p increment-failed
    =goal>
      ISA         goal
      state       increment
      state       move
    ?retrieval>
      buffer      failure
  ==>
    =goal>
      ISA         goal
      state       increment-failure
  )

(p increment
    =goal>
      ISA         goal
      state       increment
      coor        =coor
    =retrieval>
      ISA         sequence
      identity    =coor
      next        =next
  ==>
    =goal>
      ISA         goal
      state       move
      coor        =next
    +retrieval>
      ISA         sequence
      identity    =next
  )

(p outline-end
    =goal>
      ISA         goal
      state       move
      coor        =coor
    =imaginal>
      ISA         outline
      =coor       nil
  ==>
    =goal>
      ISA         goal
      state       success
  )

(goal-focus goal)
(spp decide-over :u 13)
(spp decide-under :u 13)
(spp force-over :u 10)
(spp force-under :u 10)

(spp pick-another-strategy :reward 0)
(spp read-done :reward 20))
