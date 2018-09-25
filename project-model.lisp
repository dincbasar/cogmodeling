(clear-all)

(define-model project

(sgp :v nil :needs-mouse t :cursor-noise nil)
(sgp :esc t :rt -1 :lf 0.01 :ans 0.5 :bll 0.5 :act nil :ncnar nil)
; (sgp :esc t :rt -2 :lf 0.01 :ans 0.5 :bll 0.5 :act nil :ncnar nil)
; (sgp :esc t :rt 0 :lf 0.01 :ans 0.5 :bll 0.5 :act nil :ncnar nil)
(sgp :mouse-fitts-coeff 0.001) ; simulating hand-pen movements rather than mouse

#|
important parameters:
retrieval threshold rt
latency factor
ans for noise
bll for base level learning (dont adjust)
act is activation trace
ncnar is not very necessary (saves time if you have a lot of chunks)
mp for mismatch penalty: scale for partial matching
      how much it is penalized for a mismatch
set-similarities for first to second for example higher than first to third
|#

(chunk-type outline letter count start-coor dest-coor)
(chunk-type goal letter state number)
(chunk-type stroke p1 p2)
(chunk-type sequence identity next)
(chunk-type letter id)

(set-visloc-default screen-x lowest)
(install-device '("motor" "cursor" "mouse"))
(start-hand-at-mouse)

;; add the whole chunk to imaginal

(add-dm
  (one ISA sequence identity first next second)
  (two ISA sequence identity second next third)
  (three ISA sequence identity third next fourth)
  (four ISA sequence identity fourth next fifth)
  (five ISA sequence identity fifth next sixth)

  (c00 ISA visual-location screen-x 20 screen-y 20)
  (c01 ISA visual-location screen-x 40 screen-y 20)
  (c02 ISA visual-location screen-x 60 screen-y 20)
  (c10 ISA visual-location screen-x 20 screen-y 50)
  (c11 ISA visual-location screen-x 40 screen-y 50)
  (c12 ISA visual-location screen-x 60 screen-y 50)
  (c20 ISA visual-location screen-x 20 screen-y 80)
  (c21 ISA visual-location screen-x 40 screen-y 80)
  (c22 ISA visual-location screen-x 60 screen-y 80)

  (goal isa goal)
  (find-goal) (attend-goal)
  (start) (start-retrieval) (retrieval) (move) (click) (increment) (outline-failure)
  (increment-failure) (end) (outline-retrieval) (count)
  (move-start) (move-end) (click-start) (click-end)
  (start-coor) (dest-coor) (first) (second) (third) (fourth) (fifth) (sixth)
)

(p find-goal
    =goal>
      state       nil
    =visual-location>
    ?visual>
      state       free
  ==>
    =goal>
      state       attend-goal
    +visual>
      cmd         move-attention
      screen-pos  =visual-location
)

(p encode-goal-letter
    =goal>
      state       attend-goal
      letter      nil
    =visual>
      value       =letter
  ==>
    =goal>
      state       start-retrieval
      letter      =letter
)

(p start-retrieve
    =goal>
      ISA         goal
      state       start-retrieval
      letter      =letter
  ==>
    =goal>
      ISA         goal
      state       outline-retrieval
      number      first
    +retrieval>
      ISA         outline
      letter      =letter
      count       first
)

(p fail-retrieve
    =goal>
      ISA         goal
      state       outline-retrieval
    ?retrieval>
      buffer      failure
  ==>
    +goal>
)

(p encode-letter-outline
    =goal>
      ISA         goal
      state       outline-retrieval
      letter      =letter
      number      =count
    =retrieval>
      ISA         outline
      letter      =letter
      count       =count
      start-coor  =start-coor
      dest-coor   =dest-coor
    ?imaginal>
      state       free
      buffer      empty
  ==>
    =goal>
      ISA         goal
      state       move-start
      letter      =letter
      number      =count
    +imaginal>
      ISA         outline
      letter      =letter
      count       =count
      start-coor  =start-coor
      dest-coor   =dest-coor
    +retrieval>
      ISA         sequence
      identity    =count
)

(p move-start-coordinate
    =goal>
      ISA         goal
      state       move-start
      letter      =letter
      number      =count
    =imaginal>
      ISA         outline
      letter      =letter
      count       =count
      start-coor  =start-coor
    ?manual>
      state       free
  ==>
    !output!      (Move =start-coor)
    =goal>
      ISA         goal
      state       click-start
    +manual>
      cmd         move-cursor
      loc         =start-coor
    =imaginal>
)

(p click-mouse-start
    =goal>
      ISA         goal
      state       click-start
      number      =count
    ?manual>
      state       free
  ==>
    !output!      (Click)
    =goal>
      ISA         goal
      state       move-end
    +manual>
      cmd         click-mouse
)

(p move-dest-coordinate
    =goal>
      ISA         goal
      state       move-end
      letter      =letter
      number      =count
    =imaginal>
      ISA         outline
      letter      =letter
      count       =count
      dest-coor   =dest-coor
    ?manual>
      state       free
  ==>
    !output!      (Move =dest-coor)
    =goal>
      ISA         goal
      state       click-end
    +manual>
      cmd         move-cursor
      loc         =dest-coor
)

(p click-mouse-end
    =goal>
      ISA         goal
      state       click-end
      number      =count
      letter      =letter
    =retrieval>
      ISA         sequence
      identity    =count
      next        =next
    ?manual>
      state       free
  ==>
    !output!      (Click =next)
    =goal>
      ISA         goal
      state       outline-retrieval
      number      =next
    +manual>
      cmd         click-mouse
    +retrieval>
      ISA         outline
      letter      =letter
      count       =next
)

(p click-mouse-finish
    =goal>
      ISA         goal
      state       click-end
    ?retrieval>
      buffer      failure
    ?manual>
      state       free
  ==>
    !output!      (Click ="finished")
    +goal>
    +manual>
      cmd         click-mouse
)


(set-base-levels
  (one 10) (two 10) (three 10) (four 10) (five 10))

(goal-focus goal)
)
