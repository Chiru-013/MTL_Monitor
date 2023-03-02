module Queue where
import Clash.Explicit.Testbench
import Clash.Prelude

f (x,y) = x
g (x,y) = y
  
-- 1  = True
-- (-1) = False
-- 0  = Maybe
  
modEveryElem index value (tt1, tt2, ff1, ff2, mm1, mm2, tm1, tm2, fm1, fm2)
  | (index<= tt2) && (index>= tt1) = 1
  | (index<= ff2) && (index>= ff1) = (-1)
  | (index<= mm2) && (index>= mm1) = 0
  | (index<= tm2) && (index>= tm1) && (value == 0) = 1
  | (index<= fm2) && (index>= fm1) && (value == 0) = (-1)
  | otherwise = value
  
modify vec (tt1, tt2, ff1, ff2, mm1, mm2, tm1, tm2, fm1, fm2) = imap (\i a -> modEveryElem (fromIntegral i) a (tt1, tt2, ff1, ff2, mm1, mm2, tm1, tm2, fm1, fm2)) vec

queue vec (tt1, tt2, ff1, ff2, mm1, mm2, tm1, tm2, fm1, fm2) = (modify (f (shiftInAt0 vec (0:>Nil))) (tt1, tt2, ff1, ff2, mm1, mm2, tm1, tm2, fm1, fm2), headposnvalue)
    where
    headposnvalue = vec !! (length vec -1) 
    
queuetest vec (tt1, tt2, ff1, ff2, mm1, mm2, tm1, tm2, fm1, fm2) = (f (queue vec (tt1, tt2, ff1, ff2, mm1, mm2, tm1, tm2, fm1, fm2)), queue vec (tt1, tt2, ff1, ff2, mm1, mm2, tm1, tm2, fm1, fm2))

queue_mealy inp = mealy queuetest (0:>0:>0:>0:>0:>0:>0:>0:>Nil) inp

--import qualified Data.List as L
-- L.take 15 $ simulate @System queue_mealy [ (1,3,4,5,0,0,15,15,15,15), (15,15,15,15,15,15,15,15,15,15), (0,0,15,15,15,15,15,15,15,15),(15,15, 15,15,15,15, 5,5,7,7),(15,15, 15,15,15,15, 5,5,7,7),(15,15, 15,15,15,15, 5,5,7,7) ,(15,15, 15,15,15,15, 5,5,7,7),(15,15, 15,15,15,15, 5,5,7,7) ]
