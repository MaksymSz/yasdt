from antlr4.Token import Token

INVALID_INTERVAL = (-1, -2)

class ParseTreeVisitor(object):
    def visit(self, tree):
        return tree.accept(self)

    def visitChildren(self, node):
        result = self.defaultResult()
        n = node.getChildCount()
        for i in range(n):
            if not self.shouldVisitNextChild(node, result):
                return result

            c = node.getChild(i)
            childResult = c.accept(self)
            result = self.aggregateResult(result, childResult)

        return result

    def visitTerminal(self, node):
        return self.defaultResult()

    def visitErrorNode(self, node):
        return self.defaultResult()

    def defaultResult(self):
        return None

    def aggregateResult(self, aggregate, nextResult):
        return nextResult

    def shouldVisitNextChild(self, node, currentResult):
        return True

ParserRuleContext = None

class ParseTreeListener(object):

    def visitTerminal(self, node):
        pass

    def visitErrorNode(self, node):
        pass

    def enterEveryRule(self, ctx:ParserRuleContext):
        pass

    def exitEveryRule(self, ctx:ParserRuleContext):
        pass

del ParserRuleContext



class ParseTreeWalker(object):

    DEFAULT = None

    def walk(self, listener:ParseTreeListener, t:ParseTree):
        """
	    Performs a walk on the given parse tree starting at the root and going down recursively
	    with depth-first search. On each node, {@link ParseTreeWalker#enterRule} is called before
	    recursively walking down into child nodes, then
	    {@link ParseTreeWalker#exitRule} is called after the recursive call to wind up.
	    @param listener The listener used by the walker to process grammar rules
	    @param t The parse tree to be walked on
        """
        if isinstance(t, ErrorNode):
            listener.visitErrorNode(t)
            return
        elif isinstance(t, TerminalNode):
            listener.visitTerminal(t)
            return
        self.enterRule(listener, t)
        for child in t.getChildren():
            self.walk(listener, child)
        self.exitRule(listener, t)

    #
    # The discovery of a rule node, involves sending two events: the generic
    # {@link ParseTreeListener#enterEveryRule} and a
    # {@link RuleContext}-specific event. First we trigger the generic and then
    # the rule specific. We to them in reverse order upon finishing the node.
    #
    def enterRule(self, listener:ParseTreeListener, r:RuleNode):
        """
	    Enters a grammar rule by first triggering the generic event {@link ParseTreeListener#enterEveryRule}
	    then by triggering the event specific to the given parse tree node
	    @param listener The listener responding to the trigger events
	    @param r The grammar rule containing the rule context
        """
        ctx = r.getRuleContext()
        listener.enterEveryRule(ctx)
        ctx.enterRule(listener)

    def exitRule(self, listener:ParseTreeListener, r:RuleNode):
        """
	    Exits a grammar rule by first triggering the event specific to the given parse tree node
	    then by triggering the generic event {@link ParseTreeListener#exitEveryRule}
	    @param listener The listener responding to the trigger events
	    @param r The grammar rule containing the rule context
        """
        ctx = r.getRuleContext()
        ctx.exitRule(listener)
        listener.exitEveryRule(ctx)

ParseTreeWalker.DEFAULT = ParseTreeWalker()
