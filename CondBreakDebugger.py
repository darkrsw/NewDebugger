from utils import next_inputs, input

class CondBreakDebugger():
    def __init__(self, *, file: TextIO = sys.stdout) -> None:
        """Create a new interactive debugger."""
        self.stepping: bool = True
        self.breakpoints: Set[int] = set()

        self.breakcond: List[str] = []

        self.interact: bool = True

        self.frame: FrameType
        self.event: Optional[str] = None
        self.arg: Any = None

        self.local_vars: Dict[str, Any] = {}

        self.last_vars: Dict[str, Any] = {}

        self.original_trace_function: Optional[Callable] = None
        self.file = file


    def eval_break_cond(self) -> bool:
        ret = False

        for cond in self.breakcond:
            try:
                if True == eval(cond, self.local_vars, globals()):
                    ret = True
            except Exception as e:
                pass

        return ret

    def stop_here(self) -> bool:
        """Return True if we should stop"""
        return self.eval_break_cond() or self.stepping or self.frame.f_lineno in self.breakpoints


    def break_command(self, arg: str = "") -> None:
        """Set a breakoint in given line. If no line is given, list all breakpoints"""

        if arg:
            try:
                lineno = int(arg)
                self.breakpoints.add(lineno)
            except ValueError:
                self.breakcond.append(arg)
            except:
                pass

        self.log("Breakpoints:", self.breakpoints)
        self.log("Break conds:", self.breakcond)


    def set_command(self, arg: str) -> None:
        """Use as 'set VAR=VALUE'. Assign VALUE to local variable VAR."""

        sep = arg.find('=')
        if sep > 0:
            var = arg[:sep].strip()
            expr = arg[sep + 1:].strip()
        else:
            self.help_command("set")
            return

        vars = self.local_vars
        try:
            vars[var] = eval(expr, self.frame.f_globals, vars)
        except Exception as err:
            self.log(f"{err.__class__.__name__}: {err}")


    def attr_command(self, arg: str) -> None:
        """Use as 'attr OBJ, VAR, EXPR'. Assign VALUE to local variable VAR."""

        tokens = arg.split(',')
        if len(tokens) == 3:
            obj = tokens[0].strip()
            var = tokens[1].strip()
            value = tokens[2].strip()
        else:
            self.help_command("attr")
            return

        vars = self.local_vars

        try:
            setattr(eval(obj, self.frame.f_globals, vars), var, eval(value, self.frame.f_globals, vars))
        except Exception as err:
            self.log(f"{err.__class__.__name__}: {err}")
