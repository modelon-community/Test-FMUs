package testModels
    model noStateAssertFailureFunctionLocalVariable
        function f
            input Real t;
            output Real g;
        algorithm
            g := t;
            assert(t < 0.5, "nope", level = AssertionLevel.error)
            annotation(inline=false);
        end f;

        Real g;
    equation
        g = f(time);
    end noStateAssertFailureFunctionLocalVariable;

    model noStateAssertFailureFunctionOutputVariable
        function f
            input Real t;
            output Real g;
        algorithm
            g := t;
            assert(t < 0.5, "nope", level = AssertionLevel.error)
            annotation(inline=false);
        end f;

        output Real g;
    equation
        g = f(time);
    end noStateAssertFailureFunctionOutputVariable;
end testModels;
