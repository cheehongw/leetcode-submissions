class Solution:
    def countOfAtoms(self, formula: str) -> str:
        atom_dict = OrderedDict(sorted(self.countAtoms(formula).items()))
        return ''.join([k + str(v) if v > 1 else k for k, v in atom_dict.items()])
            

                

    def countAtoms(self, formula):
        ele_count = {}
        
        idx = 0
        while(idx < len(formula)):
            c = formula[idx]
            if (c.isupper()):
                element, count, next_idx = self.findElement(formula, idx)
                ele_count[element] = ele_count.get(element, 0) + count
                idx = next_idx
            elif (c == '('):
                bracketed_formula, count, next_idx = self.findBracketedFormula(formula, idx + 1)
                atom_counts = self.countAtoms(bracketed_formula)
                for k, v in atom_counts.items():
                    ele_count[k] = ele_count.get(k, 0) + v*count
                idx = next_idx
            else:
                print('error')
                break
        
        return ele_count


    def findElement(self, formula, start):
        end = start + 1
        while(end < len(formula) and formula[end].islower()):
            end += 1
        
        element = formula[start:end]

        num_end = end
        while(num_end < len(formula) and formula[num_end].isnumeric()):
            num_end += 1

        count = int(formula[end:num_end]) if formula[end:num_end].isnumeric() else 1

        return element, count, num_end

        
    def findBracketedFormula(self, formula, start):
        end = start
        open_brackets = 0
        while(end < len(formula) and (open_brackets > 0 or formula[end] != ')')):
            if (formula[end] == '('):
                open_brackets += 1
            if (formula[end] == ')'):
                open_brackets -= 1
            end += 1

        bracketed_formula = formula[start: end]
        
        num_end = end + 1
        while(num_end < len(formula) and formula[num_end].isnumeric()):
            num_end += 1
        
        count = int(formula[end + 1: num_end]) if formula[end + 1:num_end].isnumeric() else 1
        return bracketed_formula, count, num_end


        
