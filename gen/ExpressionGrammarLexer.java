// Generated from C:/Users/Maksym/PycharmProjects/yasdt/grammar/ExpressionGrammarLexer.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class ExpressionGrammarLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		VAR=1, SIN=2, COS=3, TAN=4, COT=5, EXP=6, LOG=7, LN=8, NUMBER=9, LOGBASE=10, 
		ADD=11, MUL=12, LPAREN=13, RPAREN=14, LBRAC=15, RBRAC=16, PLUS=17, MINUS=18, 
		TIMES=19, DIV=20, POINT=21, POW=22, UNDER=23, COMMA=24, WS=25;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"VAR", "SIN", "COS", "TAN", "COT", "EXP", "LOG", "LN", "NUMBER", "LOGBASE", 
			"ADD", "MUL", "LPAREN", "RPAREN", "LBRAC", "RBRAC", "PLUS", "MINUS", 
			"TIMES", "DIV", "POINT", "POW", "UNDER", "COMMA", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'x'", "'sin'", "'cos'", "'tan'", "'cot'", "'e'", "'log'", "'ln'", 
			null, null, null, null, "'('", "')'", "'{'", "'}'", "'+'", "'-'", "'*'", 
			"'/'", "'.'", "'^'", "'_'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "VAR", "SIN", "COS", "TAN", "COT", "EXP", "LOG", "LN", "NUMBER", 
			"LOGBASE", "ADD", "MUL", "LPAREN", "RPAREN", "LBRAC", "RBRAC", "PLUS", 
			"MINUS", "TIMES", "DIV", "POINT", "POW", "UNDER", "COMMA", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public ExpressionGrammarLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "ExpressionGrammarLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0019\u00a5\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017"+
		"\u0002\u0018\u0007\u0018\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0003"+
		"\bP\b\b\u0001\b\u0004\bS\b\b\u000b\b\f\bT\u0001\b\u0001\b\u0004\bY\b\b"+
		"\u000b\b\f\bZ\u0003\b]\b\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0004\te\b\t\u000b\t\f\tf\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0004\to\b\t\u000b\t\f\tp\u0001\t\u0001\t\u0004\tu\b\t\u000b\t\f\t"+
		"v\u0001\t\u0001\t\u0004\t{\b\t\u000b\t\f\t|\u0003\t\u007f\b\t\u0003\t"+
		"\u0081\b\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u0010"+
		"\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0013"+
		"\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0016"+
		"\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0018\u0004\u0018\u00a0\b\u0018"+
		"\u000b\u0018\f\u0018\u00a1\u0001\u0018\u0001\u0018\u0000\u0000\u0019\u0001"+
		"\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007"+
		"\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d"+
		"\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016-\u0017/"+
		"\u00181\u0019\u0001\u0000\u0004\u0001\u000009\u0002\u0000++--\u0002\u0000"+
		"**//\u0003\u0000\t\n\r\r  \u00b0\u0000\u0001\u0001\u0000\u0000\u0000\u0000"+
		"\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000"+
		"\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b"+
		"\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001"+
		"\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001"+
		"\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001"+
		"\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001"+
		"\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001"+
		"\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000"+
		"\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000"+
		"\u0000)\u0001\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0000-"+
		"\u0001\u0000\u0000\u0000\u0000/\u0001\u0000\u0000\u0000\u00001\u0001\u0000"+
		"\u0000\u0000\u00013\u0001\u0000\u0000\u0000\u00035\u0001\u0000\u0000\u0000"+
		"\u00059\u0001\u0000\u0000\u0000\u0007=\u0001\u0000\u0000\u0000\tA\u0001"+
		"\u0000\u0000\u0000\u000bE\u0001\u0000\u0000\u0000\rG\u0001\u0000\u0000"+
		"\u0000\u000fK\u0001\u0000\u0000\u0000\u0011O\u0001\u0000\u0000\u0000\u0013"+
		"\u0080\u0001\u0000\u0000\u0000\u0015\u0082\u0001\u0000\u0000\u0000\u0017"+
		"\u0084\u0001\u0000\u0000\u0000\u0019\u0086\u0001\u0000\u0000\u0000\u001b"+
		"\u0088\u0001\u0000\u0000\u0000\u001d\u008a\u0001\u0000\u0000\u0000\u001f"+
		"\u008c\u0001\u0000\u0000\u0000!\u008e\u0001\u0000\u0000\u0000#\u0090\u0001"+
		"\u0000\u0000\u0000%\u0092\u0001\u0000\u0000\u0000\'\u0094\u0001\u0000"+
		"\u0000\u0000)\u0096\u0001\u0000\u0000\u0000+\u0098\u0001\u0000\u0000\u0000"+
		"-\u009a\u0001\u0000\u0000\u0000/\u009c\u0001\u0000\u0000\u00001\u009f"+
		"\u0001\u0000\u0000\u000034\u0005x\u0000\u00004\u0002\u0001\u0000\u0000"+
		"\u000056\u0005s\u0000\u000067\u0005i\u0000\u000078\u0005n\u0000\u0000"+
		"8\u0004\u0001\u0000\u0000\u00009:\u0005c\u0000\u0000:;\u0005o\u0000\u0000"+
		";<\u0005s\u0000\u0000<\u0006\u0001\u0000\u0000\u0000=>\u0005t\u0000\u0000"+
		">?\u0005a\u0000\u0000?@\u0005n\u0000\u0000@\b\u0001\u0000\u0000\u0000"+
		"AB\u0005c\u0000\u0000BC\u0005o\u0000\u0000CD\u0005t\u0000\u0000D\n\u0001"+
		"\u0000\u0000\u0000EF\u0005e\u0000\u0000F\f\u0001\u0000\u0000\u0000GH\u0005"+
		"l\u0000\u0000HI\u0005o\u0000\u0000IJ\u0005g\u0000\u0000J\u000e\u0001\u0000"+
		"\u0000\u0000KL\u0005l\u0000\u0000LM\u0005n\u0000\u0000M\u0010\u0001\u0000"+
		"\u0000\u0000NP\u0005-\u0000\u0000ON\u0001\u0000\u0000\u0000OP\u0001\u0000"+
		"\u0000\u0000PR\u0001\u0000\u0000\u0000QS\u0007\u0000\u0000\u0000RQ\u0001"+
		"\u0000\u0000\u0000ST\u0001\u0000\u0000\u0000TR\u0001\u0000\u0000\u0000"+
		"TU\u0001\u0000\u0000\u0000U\\\u0001\u0000\u0000\u0000VX\u0005.\u0000\u0000"+
		"WY\u0007\u0000\u0000\u0000XW\u0001\u0000\u0000\u0000YZ\u0001\u0000\u0000"+
		"\u0000ZX\u0001\u0000\u0000\u0000Z[\u0001\u0000\u0000\u0000[]\u0001\u0000"+
		"\u0000\u0000\\V\u0001\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000]\u0012"+
		"\u0001\u0000\u0000\u0000^_\u0003-\u0016\u0000_`\u00050\u0000\u0000`a\u0005"+
		".\u0000\u0000ab\u0001\u0000\u0000\u0000bd\u000219\u0000ce\u000209\u0000"+
		"dc\u0001\u0000\u0000\u0000ef\u0001\u0000\u0000\u0000fd\u0001\u0000\u0000"+
		"\u0000fg\u0001\u0000\u0000\u0000g\u0081\u0001\u0000\u0000\u0000hi\u0003"+
		"-\u0016\u0000ij\u00051\u0000\u0000jk\u0005.\u0000\u0000kl\u0001\u0000"+
		"\u0000\u0000ln\u000219\u0000mo\u000209\u0000nm\u0001\u0000\u0000\u0000"+
		"op\u0001\u0000\u0000\u0000pn\u0001\u0000\u0000\u0000pq\u0001\u0000\u0000"+
		"\u0000q\u0081\u0001\u0000\u0000\u0000rt\u0003-\u0016\u0000su\u000229\u0000"+
		"ts\u0001\u0000\u0000\u0000uv\u0001\u0000\u0000\u0000vt\u0001\u0000\u0000"+
		"\u0000vw\u0001\u0000\u0000\u0000w~\u0001\u0000\u0000\u0000xz\u0005.\u0000"+
		"\u0000y{\u000209\u0000zy\u0001\u0000\u0000\u0000{|\u0001\u0000\u0000\u0000"+
		"|z\u0001\u0000\u0000\u0000|}\u0001\u0000\u0000\u0000}\u007f\u0001\u0000"+
		"\u0000\u0000~x\u0001\u0000\u0000\u0000~\u007f\u0001\u0000\u0000\u0000"+
		"\u007f\u0081\u0001\u0000\u0000\u0000\u0080^\u0001\u0000\u0000\u0000\u0080"+
		"h\u0001\u0000\u0000\u0000\u0080r\u0001\u0000\u0000\u0000\u0081\u0014\u0001"+
		"\u0000\u0000\u0000\u0082\u0083\u0007\u0001\u0000\u0000\u0083\u0016\u0001"+
		"\u0000\u0000\u0000\u0084\u0085\u0007\u0002\u0000\u0000\u0085\u0018\u0001"+
		"\u0000\u0000\u0000\u0086\u0087\u0005(\u0000\u0000\u0087\u001a\u0001\u0000"+
		"\u0000\u0000\u0088\u0089\u0005)\u0000\u0000\u0089\u001c\u0001\u0000\u0000"+
		"\u0000\u008a\u008b\u0005{\u0000\u0000\u008b\u001e\u0001\u0000\u0000\u0000"+
		"\u008c\u008d\u0005}\u0000\u0000\u008d \u0001\u0000\u0000\u0000\u008e\u008f"+
		"\u0005+\u0000\u0000\u008f\"\u0001\u0000\u0000\u0000\u0090\u0091\u0005"+
		"-\u0000\u0000\u0091$\u0001\u0000\u0000\u0000\u0092\u0093\u0005*\u0000"+
		"\u0000\u0093&\u0001\u0000\u0000\u0000\u0094\u0095\u0005/\u0000\u0000\u0095"+
		"(\u0001\u0000\u0000\u0000\u0096\u0097\u0005.\u0000\u0000\u0097*\u0001"+
		"\u0000\u0000\u0000\u0098\u0099\u0005^\u0000\u0000\u0099,\u0001\u0000\u0000"+
		"\u0000\u009a\u009b\u0005_\u0000\u0000\u009b.\u0001\u0000\u0000\u0000\u009c"+
		"\u009d\u0005,\u0000\u0000\u009d0\u0001\u0000\u0000\u0000\u009e\u00a0\u0007"+
		"\u0003\u0000\u0000\u009f\u009e\u0001\u0000\u0000\u0000\u00a0\u00a1\u0001"+
		"\u0000\u0000\u0000\u00a1\u009f\u0001\u0000\u0000\u0000\u00a1\u00a2\u0001"+
		"\u0000\u0000\u0000\u00a2\u00a3\u0001\u0000\u0000\u0000\u00a3\u00a4\u0006"+
		"\u0018\u0000\u0000\u00a42\u0001\u0000\u0000\u0000\f\u0000OTZ\\fpv|~\u0080"+
		"\u00a1\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}