module ProcessingElement where
import Clash.Explicit.Testbench
import Clash.Prelude
import Queue(queue)

f (x,y) = x
g (x,y) = y

processingElement (opcode,(tt1t, tt2t, ff1t, ff2t, mm1t, mm2t, tm1t, tm2t, fm1t, fm2t),(tt1f, tt2f, ff1f, ff2f, mm1f, mm2f, tm1f, tm2f, fm1f, fm2f)) ((write, newInst),input1,input2) = (currInst',(tt1, tt2, ff1, ff2, mm1, mm2, tm1, tm2, fm1, fm2)) where
  currInst'
    | write     = newInst
    | otherwise = (opcode,(tt1t, tt2t, ff1t, ff2t, mm1t, mm2t, tm1t, tm2t, fm1t, fm2t),(tt1f, tt2f, ff1f, ff2f, mm1f, mm2f, tm1f, tm2f, fm1f, fm2f))
  (tt1, tt2, ff1, ff2, mm1, mm2, tm1, tm2, fm1, fm2)
    | (opcode ==0) && (input1 || input2) = (tt1t, tt2t, ff1t, ff2t, mm1t, mm2t, tm1t, tm2t, fm1t, fm2t)
    | (opcode ==0)                       = (tt1f, tt2f, ff1f, ff2f, mm1f, mm2f, tm1f, tm2f, fm1f, fm2f)
  
--currInst = (opcode,QID1,QID2,DQID,(tt1t, tt2t, ff1t, ff2t, mm1t, mm2t, tm1t, tm2t, fm1t, fm2t),(tt1f, tt2f, ff1f, ff2f, mm1f, mm2f, tm1f, tm2f, fm1f, fm2f))
--currInst = (opcode,(tt1t, tt2t, ff1t, ff2t, mm1t, mm2t, tm1t, tm2t, fm1t, fm2t),(tt1f, tt2f, ff1f, ff2f, mm1f, mm2f, tm1f, tm2f, fm1f, fm2f))

-- 1  = True
-- (-1) = False
-- 0  = Maybe

-- mealy functions have type: current_state -> input -> (new_state, output)
