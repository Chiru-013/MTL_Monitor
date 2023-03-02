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

queue vec ((tt11, tt21, ff11, ff21, mm11, mm21, tm11, tm21, fm11, fm21),(tt12, tt22, ff12, ff22, mm12, mm22, tm12, tm22, fm12, fm22),(tt13, tt23, ff13, ff23, mm13, mm23, tm13, tm23, fm13, fm23)) = (modify (f (shiftInAt0 vec (0:>Nil))) (tt1', tt2', ff1', ff2', mm1', mm2', tm1', tm2', fm1', fm2'), headposnvalue)
    where
    headposnvalue = vec !! (length vec -1) 
    (tt1', tt2', ff1', ff2', mm1', mm2', tm1', tm2', fm1', fm2') = (min (min tt11 tt12) tt13,min (min tt21 tt22) tt23, min (min ff11 ff12) ff13,min (min ff21 ff22) ff23, min (min mm11 mm12) mm13,min (min mm21 mm22) mm23, min (min tm11 tm12) tm13,min (min tm21 tm22) tm23, min (min fm11 fm12) fm13,min (min fm21 fm22) fm23)
    
    
queuetest vec ((tt11, tt21, ff11, ff21, mm11, mm21, tm11, tm21, fm11, fm21),(tt12, tt22, ff12, ff22, mm12, mm22, tm12, tm22, fm12, fm22),(tt13, tt23, ff13, ff23, mm13, mm23, tm13, tm23, fm13, fm23)) = (f (queue vec ((tt11, tt21, ff11, ff21, mm11, mm21, tm11, tm21, fm11, fm21),(tt12, tt22, ff12, ff22, mm12, mm22, tm12, tm22, fm12, fm22),(tt13, tt23, ff13, ff23, mm13, mm23, tm13, tm23, fm13, fm23))), queue vec ((tt11, tt21, ff11, ff21, mm11, mm21, tm11, tm21, fm11, fm21),(tt12, tt22, ff12, ff22, mm12, mm22, tm12, tm22, fm12, fm22),(tt13, tt23, ff13, ff23, mm13, mm23, tm13, tm23, fm13, fm23)))

queue_mealy inp = mealy queuetest (0:>0:>0:>0:>0:>0:>0:>0:>Nil) inp

--import qualified Data.List as L
-- L.take 15 $ simulate @System queue_mealy [ ((1,3,4,5,0,0,15,15,15,15), (15,15,15,15,15,15,15,15,15,15), (0,0,15,15,15,15,15,15,15,15)),((15,15, 15,15,15,15, 5,5,7,7),(15,15, 15,15,15,15, 5,5,7,7),(15,15, 15,15,15,15, 5,5,7,7)) ,((15,15, 15,15,15,15, 5,5,7,7),(15,15, 15,15,15,15, 5,5,7,7),(15,15, 15,15,15,15, 5,5,7,7)) ]
