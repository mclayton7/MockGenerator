/**/
#pragma once

class QString;

class I_SimpleInterface
{
public:
	virtual ~I_SimpleInterface() {}

	virtual void voidMethodConst() const = 0;
	virtual void voidMethod() = 0;

	virtual QString qStringMethodConst() const = 0;
	virtual QString qStringMethod() = 0;

	virtual const QString& constQStringRefMethodConst() const = 0;
	virtual const QString& constQStringRefMethod() = 0;

	virtual QString& qStringRefMethodConst() const = 0;
	virtual QString& qStringRefMethod() = 0;

	virtual void voidOneIntArgMethod(int count) = 0;
	virtual void voidOneIntArgMethodConst(int count) const = 0;

	virtual void voidOneRefArgMethod(QString& stringArg) = 0;
	virtual void voidOneRefArgMethodConst(QString& stringArg) const = 0;

	virtual void voidOneConstRefArgMethod(const QString& stringArg) = 0;
	virtual void voidOneConstRefArgMethodConst(const QString& stringArg) const = 0;

protected:
	virtual void protectedButNotASignal() = 0;

protected: //signals
	virtual void simpleSignal() = 0;
	virtual void signalWithOneIntArg(int count) = 0;
	virtual void signalWithOneRefArg(const QString& stringArg) = 0;
};